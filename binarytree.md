# 이진 트리

**이진 트리는 노드가 최대 두 개인 자료구조이다.**   
**자식 노드는 부모 노드에 대한 잠초를 포함 할 수 있다.**    
**트리의 루트 노드는 모든 노드의 조상이다.**
![img_3.png](img_3.png)

## 용어에 대해서
* **노드 차수**: 자식 노드의 수
* **경로**: 한 노드에서 다른 노드에 이르는 노드의 순서
* **경로 길이**: 한 노드에서 다른 노드로 가는 간선의 수 (같으면 0)
* **형제 노드**: 부모가 같은 두 노드 
* **외부 노드**: 자식이 없는 노드 (차수가 0인 노드)
* **내부 노드**: 자식이 있는 노드 (챠수가 0인 노드)
* **노드 깊이**: 루트 노드에서 어떤 노드로 가는 경로의 길이 (루트 노드는 0)
* **노드 레벨**: 노드 깊이 + 1
* **노드 높이**: 한 노드와 단말 노드 사이의 최대 경로 길이
* **크기**: 모든 노드의 수

### 이진 트리의 두 가지 종류

`포화 이진 트리`
* 모든 내부 노드가 **두 개의 자식 노드** 보유
* 말단 노드가 **같은 깊이 또는 레벨**

`완전 이진 트리`
* *마지막 레벨을 제외*한 **모든 레벨**이 채워져 있음
* 마지막 레벨의 말단 노드는 **왼쪽에 위치**

### 이진 트리 안의 노드 개수
* 이진 트리에서는 노드 차수가 최대 **2개**에 해당한다.
* **노드의 개수**는 항상 **간선의 개수보다 1개 많다.**
* `포화 이진 트리`를 기준으로 했을 때,
    * 트리의 높이는 *h = log_2(말단 노드의 개수)*에 해당한다.
    * 말단 노드의 개수는 *2^h*이다.
    * 그 트리의 총 노드 수는 *2^h - 1*에 해당한다.
    
## 이진 트리 구현하기
* **리스트**로 트리를 구현하는 방식이 존재한다.
* 단, 리스트는 **삽입**하거나 **꺼낼 때** (O(n)을 쓰므로 **비효율적**
```python
# 구현해야 하는 기능들의 리스트?
# 1) binaryTreelist
# 2) 왼쪽에 노드 추가하기
# 3) 오른쪽에 노드 추가하기
# 4) 루트 값을 얻기
# 5) 루트 값을 세팅하기
# 6) leftchild 값
# 7) rightchild 값
def binaryTreeList(r):
    return [r, [], []] # 인덱스 1은 왼쪽, 인덱스 2는 오른족, 인덱스 0은 루트

def insertleft(root, newBranch):
    t = root.pop(1) # 어떠한 트리의 왼쪽 branch 값을 받는다
    if len(t) > 1: # 왼쪽 branch가 있으면 
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, []. []])
    return root

def insertright(root, newBranch):
    t = root.pop(2)
    if len(t) > 1: 
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# r = binaryTreeList(3)
# insertleft(r, 4)
# insertleft(r, 5)
# insertright(r, 6)
# insertright(r, 7)
# print(getRootVal(r))
# print(getLeftChild(r))
# print(getRightChild(r))
```
```python
# (노드 - 포인터) 형태의 이진 트리 구현
# 이진 트리를 구현하되, 노드 안에 포인터도 같이 구현
# 노드의 입력법, 노드의 출력법 (repr)
# 다음 노드에 추가하기
# 노드 순회하기
# leaf 여부 판단하기
# max_length 판단하기
# is_balanced

class Height(object):
    def __init__(self):
        self.height = 0

class NodeBT(object):
    def __init__(self, value = None, level = 1):
        self.value = value
        self.level = level
        self.left = None # 왜 default로?
        self.right = None # left, right는 있을 수도 없을수도

    def __repr__(self):
        return "{0}".format(self.value)

    def _add_next_node(self, value, level_here = 2):
        new_node = NodeBT(value, level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
    # 노드가 왼쪽, 오른쪽이 둘 다 있으면
    # 노드를 왼족에 추가한다
            self.left = self.left._add_next_node(value, level_here+1)
        return self # add_next_node 이후에는 트리를 반환

    def _search_for_node(self, value):
    # 전위 순회로 (pre-order) 값을 찾는다.
    # value 값을 받으면 그 값이 있는지 없는지 체크
        if self.value == value:
            return self # 그 부분을 return한다
        else:
            found = None
        if self.left:
            found = self.left._search_for_node(value)
        if self.right:
            found = found or self.right._search_for_node(value)
        return found

    def _is_leaf(self):
    # 왼쪽, 오른쪽 자식이 있나요?
        return not self.right and not self.left

    def _get_max_height(self):
        heightr, lengthl = 0, 0
        if self.right: # 만약 self.right가 있으면
            heightr = self.right._get_max_height() + 1
        if self.left:
            lengthl = self.left._get_max_height() + 1
        return max(heightr, lengthl)

    def _is_balanced(self, height = Height()): # 기본이 0
        lh = Height() #높이
        rh = Height() #높이

        if self.value is None: # self.value가 없으면
            return True

        l, r = True, True
        if self.left: # 만약 left가 존재하면
            l = self.left._is_balanced(lh)
        if self.right:
            r = self.right._is_balanced(rh)
        # Height()의 height는 두 개 중애서 한 개 max 길이를 return한다
        height.height = max(lh.height, rh.height) + 1

        if abs(lh.height - hr.height) <= 1:
            return l and r

        return False

    def _is_bst(self, left = None, right = None):
        # 이진 탐색 트리인지 확인한다 -- O(n)
        if self.value: # 만약 value가 있으면
            if left and self.value < left:
                return False
            if right and self.value > right:
                return False

            l, r = True, True
                if self.left:
                # 왼쪽은 왼쪽대로
                # 순회하면서 self.left가 먹히면, self.value 역할은 self.left로
                # 이렇게 되면 계속해서 비교한다. 언제까지? left, right가 없어질때까지
                # 중간에 한번이라도 안맞으면 나가리
                    l = self.left._is_bst(left, self.value)
                if self.right:
                    r = self.right._is_best(self.value, right)
            return l and r
        else:
            return True

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root: # root가 없으면
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)

    def is_leaf(self, value):
        node = self.root._search_for_node(value) # 원하는 value에 leaf?
        if node: # 있으면
            return node._is_leaf() # _is_leaf 메서드 자동 생성
        else:
            return False

    def get_node_level(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node.level
        else:
            return False

    def is_root(self, value):
        return self.root.value == value # 이 value가 root인가여?

    def get_height(self):
        return self.root._get_max_height()

    def is_balanced(self):
        return self.root._is_balanced()

    def is_bst(self):
        return self.root._is_best()
```
## 이진 탐색 트리 (BST)
* 노드를 정렬된 순서로 유지하는 자료구조에 해당한다.
* `이진 트리`로 이루어지며, 각 노드에는 값과 두 자식 노드에 대한 포인터 존재
* 선택적으로는 **부모 노드의 포인터**를 저장할 수 있다.
* 각 노드의 값은 **왼쪽 하위 트리의 모든 항목보다 크고**, **오른쪽 하위 트리의 모든 항목**보다 작다.
* `이진 탐색 트리`가 **균형 상태**이면 검색/삽입/삭제는 모두 `O(log n)`에 해당한다.
> 노드의 왼쪽 하위 트리에는 노드의 값보다 작은 값의 노드만 존재한다.    
> 노드의 오른쪽 하위 트리에는 노드의 값보다 큰 값의 노드가 존재한다.    
> 왼쪽과 오른쪽 하위 트리 모두 이진 탐색 트리에 해당한다.    
> 중복 노드가 존재하지 않는다.
```python
from binary_tree import NodeBT, BinaryTree
# 앞서 사용한 모듈 그대로 import

class NodeBST(NodeBT):
    # 이 부분의 경우에는 NodeBT의 __init__ 그래도 사용했음
    def __init__(self, value = None, level = 1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def _add_next_node(self, value, level_here = 2):
        new_node = NodeBST(value, level_here)
        if value > self.value: 
        # 새로운 node의 value가 root node의 value보다 높으면,
        # 이 경우는 오른쪽으로 붙는다
        # 만약 self.right가 존재하지 않으면 new_node로 추가
            self.right = self.right and self.right._add_next_node(value, level_here + 1) or new_node
        elif value < self.value:
        # 새로운 node value가 root node의 value보다 낮으면
        # 이 경우에는 왼쪽으로 붙는다
        # self.left가 존재하지 않으면 new_node를 추가
            self.left = self.left and self.left._add_next_node(value, level_here + 1) or new_node
        else:
        # 이경우에는 root node와 value 값이 같은 경우
        # 이진 탐색 트리에서는 중복을 허용하지 않음
            print("중복 노드를 허용하지 않습니다.")
        return self # 전체 트리를 프린트
    
    def _search_for_node(self, value):
        # node를 전위 순회해서 value에 맞는 노드를 찾아낸다
        if self.value == value: # 만약 루트 노드가 value와 같으면
            return self
        elif self.left and value < self.value:
            # self.left가 존재하고, 찾고자 하는 값이 루트 노드보다 작으면
            return self.left._search_for_node(value) # 여기서 sub-tree root node는 self.left
        elif self.right and self.value < value:
            # self.right가 존재하고, 찾고자 하는 값이 루트 노드보다 작으면
            return self.right._search_for_node(value) # 여기서 sub-tree root node는 self.right
        else:
            return False
            
class BinarySearchTree(BinaryTree):
    # 미처 언급되지 않은 is_root 등의 메서드는 그대로 계승
    def __init__(self):
        self.root = None
        
    def add_node(self, value):
        if not self.root:
            self.root = NodeBST(self, value)
        else:
            self.root._add_next_node(value)
```
## 자가 균형 이진 탐색 트리
* `균형 트리`는 하위 트리의 높이 차이가 1이하인 트리를 말한다.
* 하지만, **노드와 삽입 및 삭제**가 일어난다고 해서 자동적으로 균형이 유지되지는 않는다.
* 이 경우에 `편향 트리`는 이진 트리의 강점을 못살리고 `O(n)`의 시간 복잡도를 가진다.
* 이를 보완한 것이 `자가 균형 이진 탐색 트리`로, `균형도`를 통해서 조정 여부를 정한다.
> **[ 2가지 대표적인 조정 방법 ]**    
> 노드 분할 및 병합: 노드가 많으면 두 개로 분할한다.    
> 노드 회전: 간선을 회전해서, x가 y의 부모이면 y를 x의 부모, x는 y의 자식 중 하나를 거둔다.

### AVL 트리 
* `AVL 트리`는 왼쪽과 오른족의 하위 트리 높이 차이가 1보다 작은 이진 탐색 트리
* 기본적 기조는 `이진 트리 탐색` 이지만 **자가 균형 조정 메서드**가 있다.
* 균형도를 맞추기 위해서 `AVL 트리`는 오른쪽 또는 왼쪽으로 자가 회전한다.
> **[ AVL 트리의 삽입 프로세스 ]**     
> 1) 재귀 함수를 사용하여 상향식으로 구현한다.
> 2) 현재 노드는 새로 삽입될 노드의 조상 노드 중 하나
> 3) 노드가 삽입될 때 조상 노드의 높이를 갱신
> 4) 현재 노드의 균형도를 계산한다 (현재 노드의 왼쪽 하위 트리 높이 - 현재 노드의 오른쪽)
> 5) 만약 안맞으면...
>   * 균형도 1보다 큰 경우 LL, LR 케이스
>   * 균형도 -1보다 작은 경우 RR, RL 케이스

```python
class NodeAVL(NodeBT):
    def __init__(self, value = None, height = 1):
        self.value = value
        self.height = height
        self.left = None
        self.right = None

    def insert(self, value):
        # 노드를 삽입하는 경우에 해당
        new_node = NodeAVL(value)
        if value < self.value:
        # 새로운 node의 value가 root node의 value보다 낮으면,
        # 이 경우는 왼쪽으로 붙는다 (이진 탐색 트리)
        # 이진 탐색 트리므로 말단에 붙는다
            self.left = self.left and self.left.insert(value) or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) or new_node
        else:
            # 중복된 노드이므로 예외 발생
            raise Exception("중복 노드 미허용")
        
        return self.rotate(value)
    
    def rotate(self, value):
        # (조상) 노드의 높이를 갱신하는 경우 (원래 0이나 새로운 노드가 꽂힌 다음에는 0->1)
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        
        balance = self.get_balance() # 아직 나오지 않음
        
        if balance > 1:
            # CASE 1 -- LL (새 노드 값이 현재 노드의 왼쪽보다 작으면..)
            if value < self.left.value:
                return self.right_rotate() # 아직 나오지 않음
            elif value > self.left.value:
            # CASE 2 -- LR (새 노드 값이 현재 노드의 왼쪽보다 크면..)
                self.left = self.left.left_rotate() 
                return self.right.rotate()
            
        elif balance < -1 :
            # CASE 3 -- RR (새 노드 값이 현재 노드의 오른쪽 노드값보다 크면..)
            if value > self.right.value: 
                return self.left_rotate()
            # CASE 4 -- RL (새 노드 값이 현재 노드의 오른쪽 노드값보다 작으면..)
            elif value < self.right.value:
                self.right = self.right.right_rotate()
                return self.left_rotate()
        
        return self
    
    def left_rotate(self):
        '''
        [변경 전에는]
        * self.right = X
        * X.left = T2
        ============================
                 y(self)
                 /     \
                T1      X
                      /   \
                    T2    T3
        ============================
        
        [변경 후에는 -- left rotate]
        * x.left = self
        * self.right = T2
        ============================
                    X
                 /     \
            Y (self)   T3
               /   \
            T1     T2
        ============================ 
        '''
        x = self.right
        T2 = x.left
        
        x.left = self
        self.right = T2
        
        # 높이를 갱신한다
        
        self.height = 1 + max(self.get_height(self.left),
                              self.get_height(self.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))
        
        return x
        
        
```
