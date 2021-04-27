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
