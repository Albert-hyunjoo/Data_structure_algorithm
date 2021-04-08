# 파이썬 관련 고급 주제

## 멀티 프로세스와 멀티 스레드
* `메인 메모리`에서 실행되는 프로그램은 별도의 `프로세스`이다.
* `프로세스`에는 하나 이상의 `스레드`가 있으며, 이게 많아지면 `멀티 스레드` 이다.
* `프로세스`는 하나 이상이 돌아갈 수 있으며, 이것이 `멀티 프로세스` 이다.

### 멀티 프로세스
* 부모 - 자식 관계로 형성되나, 독립적이다.
* `fork` 기법을 통해서 `프로세스 를 복사하는 형식으로 진행한다.
* `프로세스` 간의 통신을 지원하는 `IPC` 를 통해 서로 커뮤니케이션해야 한다.
* `subprocess` 모듈을 통해서 파이썬 내에서 멀티 프로세스를 구현할 수 있다.

### 멀티 스레드
* `단일 프로세스`의 `멀티 스레드`는 동일한 메모리에 접근한다.
* `threading` 모듈을 통해서 파이썬 내에서 멀티 스레드를 구현한다.
* 한 프로세스에 속한 스레드는 `스택 영역`을 제외한 다른 메모리 영역을 모두 공유한다.

### [참고] 동시성과 병렬성
* `동시성`은 한 작업의 I/O 연산이 완료되는 동안, 다른 작업을 수행하여 유휴 시간을 활용하는 테크닉
* `병렬성`은 물리적으로 여러 작업이 동시에 처리ㅏ되는 것을 뜻한다.

## `subprocess` 모듈
* `subprocess`는 현재 소스 코드 내에서 새로운 프로세스를 실행할 수 있게 한다.
* `부모 프로세스`는 차례대로 다른 일을 처리하는 `자식 인스턴스`를 실행시킨다.

### `subprocess` 모듈의 예시 (출처: [네이버](https://blog.naver.com/sagala_soske/222131573917))

* `subprocess`를 통해 결과값을 다른 변수에 _출력없이_ 저장할 수 있다.
* 이 모듈을 통해서 프로세스의 입출력 및 에러 결과에 대한 리턴 코드 관리도 가능하다.

```python
# subprocess.run() 사용

import subprocess

subprocess.run(args, stdin = None, input = None, stdout = None,
               stderr = None, capture_output= False, shell = False,
               cwd = None, timeout = None, check = False, encoding = None,
               errors = None, text = None, env = None...)

# arg : 명령어를 실행한다 (** 리스트 형태)
# stdin, stdout, stderr: 표준 입력, 출력, 오류 설정 (데이터 인터셉트 가능)
# input : 입력 데이터를 설정
# capture_output : True이면 결과값 변수 별도 저장이 가능
# shell : shell 화면에 결과값 출력?
# cwd : 현재 작업 중인 워킹 디렉토리
# timeout : 지정 시간 이후에 해당 프로세스가 삭제
# check : True면 따로 예외처리 (CalledProcessError)
# encoding (= errors) : 결과값 바이너리 -> 특정 포맷
# text : True이면 결과값을 str 형태로 return
# evn : None이 아니면 지정한 새로운 환경에서 설정
```
```python
# subprocess.checkoutput() 사용
# 커맨드를 실행시키고 그 결과값을 RETURN하는 함수

import subprocess
out = subprocess.check_output([...], shell = True, encoding = 'UTF-8')
```

## `THREADING` 모듈에 대해서
* `스레드`가 여러 개가 만들어지면, `락`이나 `데드락`을 조심해야 한다.
* 이는 내부적으로 `queue` 모듈을 사용한다 (FIFO 형식으로)
* `스레드`를 `데몬` 으로 변환하면 `데몬` 스레드가 실행되지 않으면 프로그램이 종료된다.

### `threading` 모듈의 예시 [참고](https://velog.io/@nameunzz/thread-threading)
```python
# 스레딩과 큐 동시 사용법

import queue # 큐 모듈 자체가 멀티 스레딩 환경을 제공
import threading

q = queue.Queue() # 객체 생성

def worker(num): # num을 인수로 받는 worker function
    while True:
        item = q.get() # 큐로부터 FO된 값을 받고
        if item is None:
            break # 아이템이 없으면 그 즉시 종료
        # 작업을 처리한다.
        print("스레드 {0}: 처리 완료 {1}".format(num+1, item))
        q.task_done()

if __name__ == "__main__": # worker 스레드 5를 미리 만들어놓음
    num_worker_threads = 5 # 스레드 5개로 배정
    threads = [] 
    for i in range(num_worker_threads):
        t = threading.Thread(target = worker, args = (i,))
        t.start()
        threads.append(t)

for item in range(20):
    q.put(item)

q.join() # 모든 작업이 끝날 때까지 block

# stop the thread
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
```

## 뮤텍스와 세마포어

### 뮤텍스 (`mutex`)
* `뮤텍스 (mutex)`는 `동시성 제어 정책`을 강제하기 위한 장치이다.
* `뮤텍스`는 정수로, 숫자가 1 감소되면 잠금, 1 증가하면 언락되는 형식으로 장치
```python
from threading import Thread, Lock
import threading

def worker(mutex, data, thread_safe):
    if thread_safe: # thread_safe = True면
        mutex.acquire() # 자원 엑세스 직전에 lock acquire
    try:
        print("스레드 {0}: {1}\n".format(threading.get_ident(), data)) # 스레드 식별자와 데이터
    finally:
        if thread_safe:
            mutex.release() # try에서 오류 상관없이 lock 해체

if __name__ == "__main__": # 일할 스레드 설정
    threads = []
    thread_safe = False # 원래는 True여야 한다
    mutex = Lock() # lock 객체를 획득
    for i in range(20): # 스레드 20개
        t = Thread(target = worker, args = (mutex, i, thread_safe))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
```

### 세마포어 (`semaphore`)
* 세마포어 `semaphore` 는 `뮤텍스` 보다 일반적인 개념이다.
* 1보다 큰 수로 시작할 수 있으며, 이는 한번에 자원에 접근 가능한 스레드의 수
* `뮤텍스`가 락과 언락을 지원하듯, `세마포어`는 대기와 신호를 지원한다.
* 즉, 여러 개의 스레드가 있을 때 한 번에 몇 개의 스레드가 들어갈 건지를 조절하는 게 `세마포어`
```python
# 세마포어 스레드풀을 생성해서 세마포어작업

import threading
import time

class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()
    
    def acquire(self, name):
        with self.lock:
            self.active.append(name) # name을 얻는 기능
            print("획득 : {0} | 스레드 풀: {1}\n".format(name, self.active))
    
    def release(self, name):
        with self.lock: # 즉, self.lock이 활성화되어 있을 때
            self.active.remove(name)
            print("반환: {0} | 스레드 풀: {1}\n".format(name, self.active))

def worker(semaphore, pool): # 세마포어, 즉 한번에 몇개의 스레드까지?
    with semaphore:
        name = threading.currentThread().getName()
        pool.acquire(name) # ThreadPool class의 인스턴스 갖고 하나 acquire
        time.sleep(1)
        pool.release(name)

if __name__ == "__main__":
    threads = []
    pool = ThreadPool() # acquire, release name 실행 가능
    semaphore = threading.Semaphore(3) # 한번에 3개까지만 스레드가 접근
    for i in range(10): # 일단 스레드는 10개
        t = threading.Thread(target = worker, name = "스레드 " + str(i+1), args = (semaphore, pool))
        t.start()
        threads.append(t)
    for t in threads: # t.append해서 돌리고 thread 안의 모든 t에 대해 join으로 stop
        t.join()
```
