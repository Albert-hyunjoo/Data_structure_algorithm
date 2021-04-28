# 트리의 순회
* `순회`는 트리 또는 그래프 같은 구조에서 객체를 방문하는데 주로 사용되는 알고리즘이다.
* **모든 노드**를 방문하거나, **특정 노드**만 방문하는 법 둘 다 포함된다.

## 깊이 우선 탐색 (DFS)
* 특정한 트리나 그래프에서 **깊이를 우선**해서 탐색하는 알고리즘이다.
* 그래프는 (높이가 없으므로) 방문한 노드를 표시한다.
* 이 탐색의 시간 복잡도는 `O(도달 가능한 노드 수 + 도달한 노드 나가는 간선 수)`
* `깊이 우선 탐색`의 경우에는 `후입선출 (LIFO)` 형태의 스택을 사용한다 (위에서만 `pop`)

### 전위 순회 (Pre-order Traverse)
* `전위 순회`는 **루트 노드, 왼쪽 노드, 오른쪽 노드** 순으로 방문한다.
```python
# 전위 순회의 정석
def preorder(root):
    if root != 0: # 루트가 0이 아니면
        yield root.value # root.value를 출력하고
        preorder(root.left)
        preorder(root.right)
```
### 후위 순회 (post-order Traverse)
* `후위 순회`는 **왼쪽 노드, 오른쪽 노드, 루트 노드** 순으로 방문한다.
```python
# 전위 순회의 정석
def postorder(root):
    if root != 0: # 루트가 0이 아니면
        preorder(root.left)
        preorder(root.right)
        yield root.value
```

### 중위 순회 (in-order Traverse)
* `중위 순회`는 **왼쪽 노드, 루트 노드, 오른쪽 노드** 순으로 방문한다.
```python
# 전위 순회의 정석
def inorder(root):
    if root != 0: # 루트가 0이 아니면
        preorder(root.left)
        yield root.value
        preorder(root.right)
```

## 너비 우선 탐색 (BFS)
* `너비 우선 탐색`은 트리 또는 그래프에서 **너비**를 우선하여 탐색한다.
* 더 깊은 노드를 순회하기 전에 **특정 깊이의 노드**를 모두 먼저 순회한다.
* `너비 우선 탐색`은 우선적으로 **시작 노드에서 특정 노드**에 도달하는 **최단 경로**이다.
* `너비 우선 탐색`의 구현은 방문한 노드를 저장하는 데 **리스트**를 사용하고, 방문 안 한 노드는 `FIFO` 큐에 저장한다. 

## 트리 순회 구현하기
* **이진 트리 및 이진 탐색 트리 클래스**를 사용하며, `반복문`과 `재귀`를 주로 사용한다.
```python
from collections import deque
from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTransversalIterative(BinarySearchTree):
    
    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current: # stack이나 current가 있으면
            if current: # 만약 current가 있으면
                stack.append(current)
                current = current.left
            else:
                current = stack.pop() 
                nodes.append(current.value)
                current = current.right
        return nodes

    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack and current:
            if current:
                nodes.append(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes

    def preorder2(self):
        nodes = []
        stack = [self.root] # 미리 집어넣는다
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.value)
                stack.append(current.right)
                stack.append(current.left)
        return nodes
    
    def BFT(self):
        current = self.root # root를 정하고
        nodes = [] # nodes 리스트를 저장한 다음에
        queue = deque() # 큐를 생성 (FIFO)
        queue.append(current) # 일단 queue에 current = root를 저장한다음
        while queue: # queue 안에 있으면 
            current = queue.popleft() 
            # current = queue
            # root node에서 빠지면 다음 노드로 이동 (1->2)
            nodes.append(current.value)
            # 그 다음에는 새로운 root를 바탕으로 left, right
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes
```
```python
# 재귀 방식을 통해서 구현하는 방법도 있다.
from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTransversalRecursively(BinarySearchTree):
    
    def __init__(self):
        self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []
        self.nodes_post = []
        self.nodes_in = []

    def BFT(self):
        # 너비 우선 탐색의 사례
        # 여기서는 재귀를 사용하지 않는다
        
        # 여기서는 기본적으로 root.level = 1로 가정해서 시작
        # queue는 LIFO로, 먼저 들어온 것들이 먼저 나가고, stack과는 다르다.
        # queue안에다가 root를 머저 넣고,
        # current_level은 그 self.root.level에 해당한다.
        self.root.level = 1
        queue = [self.root]
        current_level = self.root.level

        # len(queue)가 0이 되지 않는 선에서
        while len(queue) > 0:
            # queue에서 맨 앞의 것을 뽑아내고
            current_node = queue.pop(0) # queue에서 맨 앞의 하나를 추출
            # 그 node가 현재 훑는 위치와 다르면
            if current_node.level > current_level:
            # 만약 현재 노드 레벨이 다르면
            # current_level += 1를 해서 맞춘다
                current_level += 1
            self.nodes_BFS.append(current_node.value)
            
            # 만약 current_node를 기준으로 left가 있으면
            # current_node의 left를 root node, 즉 current_node로 만들고
            # 이를 연산 리스트 (append) 에 추가한다 (left)
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        
        return self.nodes_BFS
    
    def inorder(self, node = None, level = 1):
        if not node and level == 1: # 노드가 없고, level == 1이다.
            node = self.root
        if node: 
            self.inorder(node.left, level + 1) # 왼쪽으로 갔다가
            self.nodes_pre.append(node.value) # 값 추가하고
            self.inorder(node.right, level + 1) # 다음 인덱스로 넘어가기
        return self.nodes_in
    
    def preorder(self, node = None, level = 1):
        if not node and level == 1:
            node = self.root
        if node: # 노드가 존재하면
            self.nodes_pre.append(node.value)
            self.preorder(node.left, level + 1)
            self.preorder(node.right, level + 1)
        return self.nodes_pre
    
    def postorder(self, node = None, level = 1):
        if not node and level == 1:
            node = self.root
        if node:
            self.postorder(node.left, level + 1)
            self.postorder(node.right, level + 1)
            self.nodes_post.append(node.value)
        return self.nodes_post
```
## 연습문제 : 최소 공통 조상 (LCA)
* `최소 공통 조상` 문제는 두 개의 node가 **상위 레벨에서 가장 먼저 만나는** 공통 노드를 찾는다.
* 문제를 해결하는 알고리즘은 다음과 같은 프로세스로 진행한다.    
> 1. 중위 순회를 통해서 사전에 리스트를 추출해놓고
       * 중위 순회를 통해서 리스트가 출력된다면 `왼쪽 루트 -> 가지` 순으로 
> 2. 만약 `최소 공통 조상` 노드가 두 개의 노드 중 **작은 것보다 작으면** **두 칸 아래**로
> 3. 만약 `최소 공통 조상` 노드가 **큰 노드보다 크면** **한 칸 아래**로 탐색
> 4. `최소 공통 조상` 노드가 **사이**에 있으면 **그 값을 출력**

```python
# LCA 알고리즘 방식
# input은 총 3개로, path, lower_value, high_value
# path는 중위 순회 방식으로 순회된 리스트
# lower value는 찾고자 하는 노드 중에 작은 노드
# higher value는 찾고자 하는 노드 중에 큰 노드

from transversal_BST_recursively import BSTwithTransversalRecursively

def find_ancestor(path, lower_value, higher_value):
    # 사전에 트리는 전위 순회가 되어있어야 한다.
    # 리스트를 통해서 lower value, higher_value 범위를 조사
    # current_value를 추출해낸다.
    while path:
        current_value = path[0]
        if current_value < lower_value:
            try:    
                path = path[2:]
            except:
                return current_value
        elif current_value > higher_value:
            try:
                path = path[1:]
            except:
                return current_value
        elif lower_value <= current_value <= higher_value:
            return current_value
```