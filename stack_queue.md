# 추상 데이터 타입

* `추상 데이터 타입 (ADT)`는 유사 구조를 가진 자료 구조에 대한 수학적 모델을 말한다.
* 즉, 클래스는 다를지라도 **기능적으로 동일한** 자료구조가 가능하다.
* 자료구조는 `연속` 형태와 `연결` 방식의 2가지로 크게 나뉠 수 있다.

## 스택 (stack)
* `스택`은 말 그대로 **아래에서 위로 쌓이는** 방식의 자료구조이다 (LIFO)
* 기능은 크게 **5가지**로 나뉘며, 시간 복잡도는 모두  `O(1)`에 해당한다.
    1) `push` : 스택의 **맨 끝**에 새로운 항목을 삽입한다
    2) `pop` : 스택 맨 끝의 항목을 **반환하는 동시에 제거**한다.
    3) `top/peek` : 스택의 **맨 끝**에 위치한 항목을 조회한다.
    4) `empty` : 스택이 비어있는지의 여부를 Boolean 형식으로 표시한다.
    5) `size` : 스택의 크기를 확인한다.
* `스택`의 경우에는 `깊이 우선 탐색 (DFS)`에서 주로 쓰이는 방식이다.
```python
# 배열로서의 스택
class Stack(object):
    def __init__(self):
        self.items = [] # 빈 리스트를 기본으로
    def isEmpty(self):
        return not bool(self.items) # self.item이 있으면 No, 아니면 Yes
    def push(self, value):
        self.items.append(value)
    def pop(self): # 반환 후에 제거
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is Empty.")
    def size(self):
        return len(self.items)
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is Empty.")

    def __repr__(self):
        return repr(self.items) # 출력이 가능한 표현
``` 
```python
# 노드 컨테이너로서의 스택
class Node(object): # 노드를 생성
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None # head를 박고
        self.count = 0 # count로 세면서 간다
    
    def isEmpty(self):
        return not bool(self.head) # 있냐 없냐만 판단하면 OK
    
    def push(self, item):
        # 맨 위에 추가되는 것이 head로 가게 된다.
        # Node(새로운 아이템이 생성되고 이전 self.head로 point 후에)
        # 이거를 가지고 self.head로 새로 assign한다.
        self.head = Node(item, self.head)
        self.count += 1 # count 1개가 늘어난다.
    
    def pop(self):
        if self.count > 0 and self.head: # count가 0보다 높고, self.head가 있으면 (value가 있으면)
            node = self.head # node로 박고 
            self.head = node.pointer # head를 내리고 (제거)
            self.count -= 1
            return node.value
        else:
            print("stack is empty.")
    
    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Stack is empty.")
    
    def size(self):
        return self.count
    
    def _printlist(self):
        node = self.head # 맨 위가 head로 설정을 하고
        while node: # node가 있으면
            print(node.value, end = '') # value 프린트를 하고
            node = node.pointer # node.pointer -> 즉 다음으로 이동
        print()
```

## 큐 (Queue)
* `큐`는 **항목이 들어온 순서**대로 접근하는 자료 구조이다. (FIFO)
* 배열의 인덱스는 `큐`와 마찬가지로 제한되며, 관련 기능의 시간 복잡도는 `O(1)` 이다.
    1) `enqueue` : 큐 뒤쪽에 항목을 삽입한다
    2) `dequeue` : 큐 앞쪽의 항목을 반환한다음, 제거한다.
    3) `peek/front` : 큐 앞 쪽의 항목을 조회한다.
    4) `empty` : 큐가 비어있는지를 확인한다.
    5) `size` : 큐의 크기를 확인한다.
* `큐`의 경우에는 `너비 우선 탐색 (BFS)`에서 주로 쓰이는 방식이다.

```python
# 배열로서의 큐
# 싱클 큐를 쓰는 경우
class queue(object):
    def __init__(self):
        self.items = [] # 빈 리스트를 기본으로
        
    def isEmpty(self):
        # self.item이 있으면 No, 아니면 Yes
        return not bool(self.items)
    
    def enqueue(self, item):
        # 여기서 하나씩 다 밀리므로 O(n)의 비효율 발생
        self.items.insert(0, item)
        
    def dequeue(self): # 반환 후에 제거
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is Empty.")
            
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is Empty.")

    def __repr__(self):
        return repr(self.items) # 출력이 가능한 표현
``` 
```python
# 배열로서의 큐
# 더블 큐를 쓰는 경우
# inbox, outbox를 따로 만들어서 필요시에만 왔다갔다
class queue(object):
    def __init__(self):
        # 빈 리스트를 기본으로
        # in stack와 out stack을 따로 형성
        self.in_stack = []
        self.out_stack = []
        
    def _transfer(self): # 아예 옮겨버리는 것
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        # in_stack에 데이터를 집어넣는다
        return self.in_stack.append(item)
    
    def dequeue(self):
        # 만약 self.out_stack에 아무것도 없으면
        # in_stack에서 transfer를 받고
        # 만약 self.out_stack이 있으면
        # self.out_stack.pop() => 스택이므로 O(1)
        # 이것도 안되면 queue is empty
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is Empty!")
    
    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is Empty!")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is Empty!")
    
    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))
```
```python
# 노드 컨테이너로서의 큐

class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = None
        self.pointer = None
        
class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        # self.head가 존재하는가? 있으면 Empty
        return not bool(self.head)

    def dequeue(self):
        # dequeue는 앞의 것이 먼저 빠진다.
        # 즉, 앞의 head가 그 다음 포인터로 바뀌고
        # 앞의 것은 자동적으로 소실
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is Empty!")
    
    def enqueue(self, value):
        # enqueue는 뒤에서 추가된다
        # self.tail에서 붙는 경우!
        node = Node(value)
        if not self.head:
            # head가 존재하지 않으면 (0->1)
            self.head = node
            self.tail = node 
        else:
            # self.tail이 있으면
            # [==|=] <- (pointer) [==|=] (self.tail)
            # [==|=] <- [==|=] <- (pointer) [==|=] (new) (self.tail)
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1
    
    def size(self):
        return self.count
    
    def peek(self):
        return self.head.value
    
    def print(self):
        node = self.head
        while node:
            print(node.value, end = '')
            node = node.pointer
        print()         
```