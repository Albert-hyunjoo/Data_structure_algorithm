# 다양한 정렬 알고리즘

* 어떠한 무작위의 배열을 크기가 작은 순서대로 재배열하는 것을 def bubble_sort(seq):
  length = len(seq)-1
  for number in range(length, 0, -1):
  for i in range(number):
  if seq[i] > seq[i+1]:
  seq[i], seq[i+1] = seq[i+1], seq[i]
  return seq정렬`이라고 한다.
* 가장 원시적인 형태는 모두 훑어서 작은 순서를 앞으로 놓는 것이지만, 이 알고리즘은 `O(n^2)` 복잡도이다.
* `제자리 정렬`은 정렬 안에서 인덱스를 이동해 용량을 덜 먹는 정렬 알고리즘
* `안정적 정렬`은 데이터 요소의 상대적인 순서를 보존하는 알고리즘

## 2차 정렬

### 거품 정렬 (Bubble Sort)
* `거품 정렬`의 기본적 알고리즘은 **인접한 두 항목**을 정렬하는 것
* 인접한 항목을 한번씩 비교해서 작은 것을 계속적으로 왼쪽으로 옮기는 개념이다.
* **OUTER LOOP**와 **INNER LOOP**를 설정하는 형식으로 코드를 구현
* 시간 복잡도는 최악의 경우 `O(n^2)`이지만, 코드가 비교적 단순하게 구현된다.
```python
# 예를 들어서 4라면, 3번 돌아서 비교, 2번 돌아서, 1번 돌고...
# 다시 3으로 돌아가서 2번 돌아서 비교, 1번 돌아서 비교...
def bubble_sort(seq):
    length = len(seq)-1
    for number in range(length, 0, -1):
        for i in range(number):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq
```

### 선택 정렬 (Selection Sort)
* `선택 정렬`은 리스트에서 가장 작거나 큰 항목을 찾아서 첫번째와 위치 변경 후,    
그 다음 항목을 찾아서 두 번째 항목과 위치를 변경한다.
* 정렬이 어느정도 되어 있더라도 이 알고리즘의 시간 복잡도는 `O(n^2)`에 해당한다.
```python
def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i # 일단 가장 첫번째 수를 min 값으로 지정
        for j in range(i+1, length): # i번째 값을 제외하고 순회하면서
          if seq[min_j] > seq[j]: # 만약 i번째보다 작은 값이 있으면
            seq[min_j], seq[j] = seq[j], seq[min_j] # 스왑한다.
                # 그 뒤로 i는 2번째 인덱스로 넘어가서 그 다음 항목과 위치를 변경
    return seq
```
### 삽입 정렬 (Insertion Sort)
* 최선의 경우에는 `O(n)`의 시간 복잡도를 지니고, 최악은 `O(n^2)`이다.
* 만약 **데이터 크기가 작고** **리스트가 정렬**되어 있으면 고급 알고리즘보다 효율이 좋다.
> **삽입 정렬 알고리즘**의 순서:    
> ① 먼저 *[1]번쨰 원소*를 *[0]번째 원소*와 비교해서 **더 크면 바꾼다**.    
> ② i는 -1로 0이 되어버리고, 이 과정에서 루프는 종료된다.    
> ③ *[2]번째 원소*를 *[1]번쨰 원소*와 비교해서 **더 크면 바꾼다**.    
> ④ *[1] (2-1)* 번째 원소를 *[0]번째 원소*와 비교해서 **더 크면 바꾼다.**
> ....
```python
def insertion_sort(seq):
    for i in range(1, len(seq)): # outer loop
        j = i
        while j > 0 and seq[j-1] > seq[j]: # inner loop
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
            print(seq)
    return seq
```
### 놈 정렬 (Gnome Sort)
* 앞으로 이동해서 잘못 정렬된 값을 찾고, 올바른 위치로 값을 교환 후 다시 뒤로!
* 최선의 경우에는 `O(n)`의 시간 복잡도이고, 평균과 최악의 경우에는 `O(n^2)`이다.
```python
def gnome_sort(seq):
    i = 0 # reference index
    while i < len(seq): # i가 오류 끝가지 가면
        if i == 0 or seq[i-1] < seq[i]: # i가 첫번쨰거나 올바르게 배열된 경우
            i += 1 # 앞으로 이동한다
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i] # 만약 아니면은 바꾸고
            i -= 1 # 이전으로 이동한다.
    return seq
```

## 선형 정렬

### 카운트 정렬 (Count Sort)
* **작은 범위의 정수**를 정렬할 때 유용하며 숫자의 발생 횟수를 카운트한다.
* 누적 카운트 갱신 후에 순서대로 숫자를 직접 배치한다.
* 카운트 정렬에서 **각 숫자 간의 간격이 크다면**, 로그 선형 제한이 걸리므로 주의!
* 숫자의 간격이 크지 않다면, 시간 복잡도는 `O(n+k)`이다.
* **동일 키를 갖는 경우**에도 원래 키의 순서를 가지므로 이 정렬 방식은 **안정적**이다.
```python
from collections import defaultdict

def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a: # a를 Outer Loop으로 순회한다.
        c[x].append(x) # x를 key로, 그 value를 x로 한다.
    for k in range(min(c), max(c) + 1): # k는 순서로 해서
        b.extend(c[k]) # c dict에서 k인 key를 extend한다 (없으면 skip)
    return b
```

## 로그 선형 정렬

### sort()와 sorted()
* 효율적인 `Timsort` 방식으로 리스트를 정렬한다.
* `sorted()`는 `reverse`, `key=len, str.lower`등의 다양한 변수를 지원

### 병합 정렬 (Merge Sort)
* 리스트를 반으로 **연속적으로 나눠** 정렬되지 않은 리스트를 **1개**가 될때까지 나누고 정렬
* 안정적이고 대규모 데이터에 적합하나, 메모리가 소모된다 (공간 복잡도가 `O(n)`)
* `연결 리스트`의 경우에는 제자리 정렬이 가능하며, 공간 복잡도는 `O(log n)`이다.
* 최악, 최선, 평균 시간 복잡도의 경우에는 `O(n log n)`이다.
```python
# 단순하게 mid로 나누어서 하는 방법
def merge_sort(seq):
    if len(seq) < 2: # seq 길이가 1이면
        return seq
    mid = len(seq)//2 # 변수 설정: mid
    left, right = seq[:mid], seq[mid:] # 변수 설정 2 : left, right
    if len(left) > 1:
        left = merge_sort(left) # 재귀로 merge_sort
    if len(right) > 1:
        right = merge_sort(right) # 재귀로 merge_sort

    res = []
    while left and right: # left와 right가 있을 때까지
        if left[-1] >= right[-1]:
            res.append(left.pop()) # 더 큰거부터 집어넣기
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res # 하나가 0이 되어버리면 어차피 left or right는 sorted된 것이다.
```
```python
# 한 함수는 정렬을 실시하고 (merge_sort_sep)
# 다른 함수는 배열을 실시하는 경우 (merge)

def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq)//2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left and not right:
        return left or right # 정렬이 없으면 not
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # i와 j가 안에 있는한
        if left[i] <= right[j]: # 만약 left에서의 i번쨰와 right의 j번째에서 right가 큰 경우
            result.append(left[i]) # 더 작은 걸 합하고
            i += 1
        else:
            result.append(right[j]) # 더 작은 걸 합하고
            j += 1 # j의 인덱스를 증가
    if left[i:]: # 한쪽이 먼저 끝나버리면 다른 한 쪽에서 진행된 인덱스부터 끝까지의 배열을 합한다
        result.extend(left[i:])
    if right[j:]:
    result.extend(right[j:])
    return result
```


