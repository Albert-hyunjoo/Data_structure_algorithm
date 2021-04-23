# 동적 계획법
* `동적 계획법`은 복잡한 문제를 **재귀**를 통해 간단한 하위 문제로 분류해서 나눈다.
* **최적 부분 구조** (했던 계산을 반복하는 부분) 와 **중복되는 부분 문제**가 있으면 사용할 수 있다.

## 메모이제이션
* `메모이제이션`은 프로그램이 동일한 계산을 반복할 때, 이전에 계산한 값을 **메모리에 저장**하여 **동일한 계산의 반복 수행을 제거**하여 프로그램의 속도를 빠르게 한다.

### 피보나치 수열의 예시
```python
# 피보나치 수열은 fib(1), fib(2).. 등의 중복이 존재
def fib3(m,n):
    if m[n] == 0: # 0일때만 실행! -> 있으면 그냥 load
        m[n] = fib3(m, n-1) + fib3(m, n-2)
    return m[n]

def test_fib3(n):
    m = [0] * (n+1) # 구하고자 하는 전체 리스트를 만들고
    m[0], m[1] = 1, 1 # 초기값 설정을 한 다음에
    print(fib3(m,n))
```
## 연습문제

### 최장 부분 증가열
```python
# expected IN : LIST 등의 SEQ 형식
# expected OUT : 증가하는 증가열의 최대 길이

# 동적 계획법으로 실행
def dp_longest_inc_subseq(seq):
    L = [1] * len(seq) # 일단 파악하고자 하는 리스트 생성
    for cur, val in enumerate(seq): # seq를 순회
        for pre in range(cur): # 이전 index의 element를 순회
            if seq[pre] <= val: # 만약 그 pre가 value보다 크면
                L[cur] = max(L[cur], 1+L[pre]) 
                # 그 L[cur]에 대해서 자기보다 큰 값의 인덱스 + 1나 자기 인덱스 중에서 최대값
                # 왜? 리스트 안에는 다양한 증가 부분열이 존재하며
                # 그 증가 부분열의 최대로 가야 가장 긴 길이의 오름차순이 정의됨
    return max(L)
```
```python
# 메모이제이션 방식으롯 설명한다
def memoized_longest_inc_subseq(seq):
    def L(cur): # L(cur) 함수를 통해서 위의 cur값을 return
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1+L(pre))
        return res
    # seq의 모든 부분을 L(i)으로 돌려서 L(i) 값의 max를 return
    # 위의 방법과 유사한 방식이나, 이것도 반복하는 부분을 캐싱해서 저장한다.
    return max(L(i) for i in range(len(seq)))
```
