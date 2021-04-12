# 추상 데이터 타입 (2)

## 데크 (Deque)
* `스택`과 `큐`의 결합체로, **양쪽 끝**에서 **조회, 삽입, 삭제**가 가능하다.
* `Deque`는 앞서 말한 `큐`를 오버라이드함으로써 구현할 수 있다.
```python
from queue import Queue

class Deque(Queue):
    # 비효율적인 데크 -> 삽입 및 삭제가 O(n) 
    # 메서드 오버라이드로 Queue의 메서드를 계승
    # 추가하는 경우에 해당한다.
    def enqueue_back(self, item):
        self.items.append(item)
    
    def dequeue_front(self):
        # 앞이 빠져버린다.
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty.")
```
```python
from collections import deque
# 효율적인 데크 -> 이중 연결 리스트에 해당

q = deque(["버피", "잰더", "윌로"])

# deque를 사용하면 데크의 크기를 limit걸 수 있다.
q1 = deque(maxlen = 4)

# deque를 통해서 모든 요소를 1개씩 뒤로 옮긴다.
q.rotate(1)
```

## 우선순위와 힙 (heap)
* `우선순위 큐`는 큐와 비슷하지만, 항목별로 **우선순위**가 존재한다.
* `우선순위 큐`는 `힙` 이라는 형태로 생성하여 진행한다.

### 힙 (heap)
* `힙`은 **각 노드가 하위 노드보다 작은 이진 트리**이다.
* 이진 트리에 수정이 이루어질 때, 이를 다시 만드는 복잡도는 **O(log n)** 이다.
* `힙`은 리스트에서 가장 **작거나 큰 요소에 반복적으로 접근**할 때 유용하다.
* 최소/최대 힙은 시간 복잡도가 `O(1)`이고, 나머지 기능은 `O(log n)` 이다.

### heapq 모듈에 대해
* `heapq (.heapify)` 모듈은 `O(n)` 시간 동안에 리스트를 `힙`으로 전환한다.
* `heapq.heappush()..` 메서드를 통해서 `힙`을 항목에 삽입한다.
* `heapq.heappop()..` 메서드를 통해서 힙에서 **가장 작은 항목을 제거 후 반환**한다.
* `heapq.heappushpop(heap, item)` 메서드로 새 항목을 `힙`에 추가하고 가장 작은 항목을 제거 후 반환.
* `heapq.heapreplace(heap, item)` 메서드로 작은 항목을 제거/반호나 후에 새 항목을 추가한다.
* `heapq.merge(....)`을 통해서 반복 가능한 객체를 합해서 하나의 `이터레이터`를 생성한다.

### 최대의 힙 구현하기
* `최대 힙`의 경우에는 다음의 규칙이 적용된다고 가정한다.
    1) 어떤 부모 인덱스 `i`의 자식은 각각 왼쪽은 `(i*2)+1`과 `(i*2)+2` 이다.
    2) 총 `힙`의 길이를 반으로 나누어 (`//`) `아래에서 위로` 재귀로 순회하면서 `skip`, `swap`을 결정한다.

```python

class Maxheap(object):
    
    def __init__(self):
        self.data = [None]
    
    def maxheapify(self, i):
        left = 2*i
        right = 2*i + 1
        smallest = i
        
        # 일단 존재는 하니? 
        # 그리고 너의 부모보다 value가 어떠니
        if left < len(self.data) and self.data[i] < self.data[left]:
            smallest = left
        # 일단 존재는 하니? 
        # 그리고 너의 부모보다 value가 어떠니
        if right < len(self.right) and self.data[i] < self.data[right]:
            smallest = right
        # 만약 smallest에 변동이 생기면
        if smallest != i: 
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i] 
        self.maxheapify(smallest) # 재귀를 실시해서 올라가기        
    
    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        
        while i > 1: # 루트 노드까지 딸려 올라간다
            if self.data[i] > self.data[(i//2)]:
                self.data[i], self.data[(i//2)] = self.data[(i//2)], self.data[i]
                i = i//2
            else:
                break
    
    def remove(self):
        # remove의 기능은? leaf를 제거?
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxheapify(1)
        else:
            data = None
        return data
    
```