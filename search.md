# 검색 (Search)

## 정렬되지 않은 배열
* **배열이 정렬되지 않**거나, `연결 리스트`같이 **동적인 입력**이 할당된 경우 사용

### 순차 검색
* 차례로 요소를 검사하면서 있는지 없는지를 찾아보는 형식
* 평균적인 시간 복잡도는 `O(N/2)`이고, 최선은 `O(1)`, 최악은 `O(n)`
* 만약 찾고자 하는 요소가 리스트에 없으면 최선/최악/평균 시간 복잡도 모두 `O(n)`
```python
# 일반적인 순차 검색
# 리스트가 정렬되어 있지 않은 경우
def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False
```
```python
def ordered_sequential_search(seq, n):
    # 만약 찾고자 하는 n이 이미 item보다 높으면 그 이후는 X 
    for item in seq:
        if item > n:
            return False
        if item == n:
            return True
    return False
```

### 빠른 선택과 순서통계량
* `퀵 정렬`을 약간만 변형해서 리스트에서 k번째로 작은 항목을 찾는다.
* 이러한 숫자 k는 k번째의 `순서통계량`이라고 부른다.
* 이 검색의 시간복잡도는 `O(n) = O(n) + O(n/2) + O(n/4)..`로 최악은 `O(n)`

```python
def quick_select_cache(seq, k):
    # 만약 seq가 길이가 2 미만이면 바로 k 프린트
    len_seq = len(seq)
    if len_seq < 2:
        return seq[0]
    
    # 피벗은 무작위 선택이 가능하지만
    # 편의를 위해서 일단 중간으로 나눠놓음
    ipivot = len_seq//2
    pivot = seq[ipivot]
    
    # smaller list는 x의 값이 pivot보다 작거나 같고, ipivot과는 같지 않은 것
    # larger list는 x의 값이 pivot보다 크고, ipivot과는 같지 않은 것
    smallerList = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    largerList = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    m = len(smallerList)
    if k == m: # 만약 smallerList의 길이가 k와 같으면
        return pivot # 피벗을 출력
    elif k < m: # 만약 smallerList의 길이와 k보다 작으면
        return quick_select_cache(smallerList, k)
    else: # 만약 smallerList의 길이보다 k가 크면 largerList로 넘어감
        return quick_select_cache(largerList, k-m-1)
```
## 정렬된 배열

### 이진 검색
* 이진 검색은 `정렬된 배열` 내에서 **지정된 입력값의** 키를 찾는다.
* 알고리즘의 단계에서 **입력값**과 **배열 중간 요소**를 비교해서, 일치하면 위치를 반환
* 만약 작거나 크면 **각 하위 배열**에서 **검색 과정을 반복**한다.
* `이진 검색`의 시간 복잡도는 `O(log n)` 이다.
```python
# 재귀함수를 갖고 이진 검색 검진
def binary_search_rec(seq, target, low, high):
    if low > high:
        return None
    mid = (low + high)//2
    if target == seq[mid]:
        return mid
    elif target < seq[mid]:
        return binary_search_rec(seq, target, low, mid-1)
    else:
        return binary_search_rec(seq, target, mid+1, high)
```
## 연습 문제

### 행렬 검색 (Array Search)
* `행렬 검색`의 전제는 각 행과 열이 **정렬된** 상태여야 한다.
* 즉, 모든 행은 왼쪽에서 오른쪽으로 정렬되며 열은 위에서 아래로 정렬된다.
* 이 검색의 시간복잡도는 선형으로 `O(m+n)`이다.
```python
def find_elem_matrix_bool(m1, value):
# 입력값을 받으면 행렬과 value를 찾는다.
    found = False
    row = 0
    col = len(m1[0]) - 1
    while row < len(m1) and col >= 0:
        if m1[row][col] == value:
            found = True
            break
        elif m1[row][col] > value:
            col -= 1
        else:
            row += 1
    return found
```
### 단봉형 배열 (Unimodel)
* `단봉형 배열`은 값이 증가했다가 다시 감소하는 곡선인 배열이다.
* 여기서 이진 검색을 통해서 배열 안에서의 **최대값**을 찾을 수 있다.
```python
# 만약 seq[mid-1] < seq[mid] < seq[mid+1] 이면 오른쪽에 최대값이 존재
# 만약 seq[mid-1] > seq[mid] > seq[mid+1] 이면 왼쪽에 최대값이 존재
# 만약 seq[mid-1] < seq[mid] > seq[mid+1] 이면 최대값

def find_max_unimodel_array(A):
    if len(A) <= 2:
        return None
    left = 0
    right = len(A) - 1
    while right > left + 1:
        mid = (left+right)//2
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return A[mid]
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            left = mid
        else:
            right = mid
    return None
```
### 제곱근 구하는 법
```python
# n의 제곱근은 이진 검색으로 mid값의 제곱으로 찾는다 (error 범위내)
# ex) 10의 제곱근을 구하는 경우에는?
# 1) 1~10 사이의 중간값 5를 기준으로 제곱 시행
# 2) 5 * 5 = 25이므로, upper = mid (1~5)
# 3) 1~5 사이의 중간값 2.5를 기준으로 제곱 시행
# 4) 2.5 * 2.5 = 6.25 이므로 < 10
# 5) 2.5 ~ 5 => 3.5
# 6) 3.5 * 3.5 = 12.25 ....

def find_sqrt_bin_search(n, error = 0.001):
    # lower, upper를 정해서
    # mid는 중간값으로 곱한다
    lower = n < 1 and n or 1
    upper = n < 1 and 1 or n
    mid = lower + (upper-lower) / 2.0
    square = mid * mid

    while abs(square - n) > error:
        if square < n:
            lower = mid
        else:
            upper = mid
        # 새롭게 mid와 square를 설정한다.
        mid = lower + (upper-lower) / 2.0
        square = mid * mid
    
    return mid
```