# 모듈 (Module)
* 모듈은 `def` 를 통해 정의하며, 함수의 객체와 참조가 함께 생성된다.
* 모듈이 아무런 값을 리턴하지 않는 경우에는 `프로시져` 라고 한다.

## 스택과 활성화 레코드에 대해

* 함수가 호출될 때마다 `활성화 레코드`가 생성되며, 함수의 정보가 `스택`에 기록이 된다.
    * 함수의 정보는 `반환값, 매개변수, 지역 변수, 반환 값/주소` 등으로 구성
* 메모리 구조는 크게 `5가지의 구조`가 있으며, 여기에 따라 용량이 실시간으로 달라진다.
    1) `기계어 코드` : 바로 실행이 가능한 코드 (어셈블리어)
    2) `전역 변수` : 글로벌하게 미리 정의된 변수에 해당 
    3) `스택` : 실질적인 함수 정보가 저장되는 양 / 쌓이는 형식 (FIFO)
    4) `잔여 공간` : 힙과 스택 사이의 Available Place
    5) `힙` : 위에서 쌓이는 형식 (LIFO)
* `활성화 레코드`는 다음과 같은 순서로 `PUSH`를 실시한다.
    1) 함수의 **실제 매개변수**를 스택에 저장
    2) **반환 주소**를 스택에 저장
    3) 스택의 **최상위 인덱스**를 함수의 지역 변수에 필요한 총량 만큼
    4) 함수로 건너뛴다 (JUMP)

## 모듈의 기본값

모듈을 생성할 때, 함수 또는 메서드에서 **가변 객체가 기본값**이 되어서는 안된다

### 잘못된 경우에는,
```python
# number_list가 가변이라 축적

def append(number, number_list = []):
    number_list.append(number)
    return number_list
```
### 올바르게 고친다면,
```python
# number_list가 불변이라 축적 X

def append(number, number_list = None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    return number_list
```

## __init__.py 파일에 대해서
* 패키지는 `모듈`과 `__init__.py`가 같이 포함되어야 한다.

## __name__ 변수
* 파이썬은 `모듈`을 임포트할 때마다, `__name__` 변수를 만들어서, 모듈 이름을 저장
* 인터프리터에서 직접 import하는 것과, 터미널에서 바로 실행하면 그 차이가 있다.

## 컴파일된 바이트코드 모듈

* 컴파일러가 사용하는 `바이트 컴파일 코드`는 프로그램 로딩 시간을 줄이기 위해
* 주로 `-O` 플래그를 사용해 인터프리터 호출 시에는, `.pyo` 형식으로 파일이 저장
* `.pyo` 파일은 리버스 엔지니어링이 까다로워 라이브러리로 배포할 수도 있다.

## sys 모듈 (시스템 모듈)

* `sys.path`는 모듈 검색 경로를 담은 문자열 리스트이다.
* `sys.ps1`와 `sys.ps2`는 기본 및 보조 프롬프트 문자열을 정의한다. (>>>, ...)
* `sys.argv`는 명령 줄에 전달된 인수를 프로그램 내에서 사용이 가능하다.
```python
import sys
def main():
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()
```
```python
$ python 1_sys_example.py 로미오 줄리엣
# 로미오
# 줄리엣
```
# 제어문

## 분기점: if문
* 다른 언어의 `switch`나 `case`를 대체한다.

## 반복문: for문
* 파이썬의 `for`문은 다른 언어의 `for`와 달리, 모든 시퀀스 항목을 순회한다.

## 참과 거짓: True and False
* 파이썬에서 거짓은 `''`, `[]`, `{}`같이 빈 것으로 정의되며, 그 외의 모든 것은 참이다.
* `False`를 올바르게 사용하기 위한 파이썬 가이드라인에 따르면,
  1) `!=`나 `==` 로 `None`을 정의하지 않는다; 대신 `is not`을 사용한다.
  2) `if x is not none` 과 `if x` 를 잘 구별한다.
  3) `== False` 대신에 `if not x`를 사용한다.
  4) `if len seq` 보다 `if not seq`나 `if seq`를 사용한다.
  
## return과 yield의 차이
* 파이썬에서 제너레이터는 이터레이터를 작성하는 편리한 방법으로
* `__iter__`와 `__next__` 구현시 사용 가능
* `return`은 바로 반환값을 반환, 메서드 종료 후, 호출자에 값을 반환
* `yield`는 반환값을 호줄자에게 반환 후에 소진시에만 메서드가 종료
* 즉, 바로바로 반환을 하는 `return`에 비해 `next()`로 필요한 때만 값 호출이 가능

## break와 Continue
* `break`는 반복문을 그 즉시 종료시키며, `continue`는 반복문의 다음 단계로 넘어간다.
* 반복문의 `else`절에 상관없이 `break`는 바로 종료, `continue`는 `else`문 이하로 이동한다.

## 그외의 다른 메서드들
* `range()`는 특성 시작점에서 끝점까지의 숫자 리스트를 생성한다.
* `enumerate()`는 반복 간으한 객체의 인덱스 값과 항목 값의 튜플을 반환한다.
* `zip()`은 2개 이상의 시퀀스를 인수로 취해서, 1:1 대응하는 튜플 시퀀스를 생성한다.
*`filter(func, seq)`는 시퀀스의 항목 중 함수 조건이 `True`인 것만 추출한 시퀀스를 반환한다.
* `map(func, list)`는 시퀀스의 모든 항목에 함수 적용 결과를 반환한다.
* `lambda()` 는 코드 내에서 간결한 동적 함수를 지원한다.
  ```python
  area = lambda b, h: 0.5 * b * h
  area(5,4)
  ```
   ```python
  # defaultdict에서 누락된 키에 대한 기본값 생성
  import Collections
  minus_one_dict = collections.defaultdict(lambda: -1)
  point_zero_dict = collections.defaultdict(lambda: (0,0))
  message_dict = collections.defaultdict(lambda: "No Message")
  ```
# 파일 처리 메서드

## 파일의 실행 및 읽기
* `open(filename, mode, encoding)`은 파일을 읽어서 객체를 반환한다.
* `read(size)`는 파일에서 `size`만큼 읽고, 문자열로 반환한다.
* `readline()`은 파일에서 _한 줄_, `readlines()`는 모든 _데이터의 행 포함 리스트_를 반환한다.

## 파일을 작성하기
* `write()`는 데이터를 파일에 쓰고, `None`을 반환한다.
* `tell()`과 `seek(offset, from-what)`는 파일의 현재 위치를 나타내는 정수를 반환한다.
* `close()`는 파일을 닫고, 열린 파일이 차지하는 시스템 자원을 해제한다.
* `input()` 함수는 사용자의 입력을 받으며, 콘솔의 문자열을 선택적으로 지정할 수 있다.

## 3가지 시스템 조작 모듈
* `shutil`은 시스템에서 파일을 조작하는데 유리한 모듈이다.
* `pickle`은 파이썬 객체를 가져와서, 문자열 표현으로 변환 (피클링) 한다.
* `struct`는 파이썬 객체를 이진으로 변환, or 반대도 가능하다.

# 오류 처리 메서드

## 예외 처리 메서드
* `try`는 오류가 발생할 것으로 예상되는 코드를 실행하는 커맨드이다.
* 만약 예외가 발생하지 않으면 `except`문은 건너뛰지만, 발생시 이하 구문 통해 예외를 처리한다.
* 오류 여부와 관계없이 `finally`를 통해서 코드를 마무리한다.
* `raise`를 실행하면 어떠한 예외를 의도적으로 불러일으킬 수 있다.

## 예외 처리 가이드
* `raise MyError('오류 메시지')` 형식으로 오류를 처리하며, 두 개 인수 형식은 사용 지양
* 내장 예외 클래스를 적절해야 사용해야 하며, `assert`의 지나친 사용은 지양한다.
```python
# 사용가능한 포트에 연결, minimum 포트를 반환
def ConnectToNextPort(self, minimum):
  # raise로 오류를 처리하는 게 주가 되어야 하고
  if mimimum < 1024:
      raise ValueError("1025 이상의 포트를 입력하십시오.")
  port = self.FindNextOpenPort(minimum)
  if not port:
    raise ConnectionError("$d에 연결 불가합니다." % (minimum,))
  # assert는 정확도를 높일 떄만 쓰일 수 있도록
  assert port > minimum, ("예상 못한 %d 포트에 연결했습니다."" % (minimum,")...)
  return port
  ```
* 라이브러리나 패키지는 자체적인 예외를 정의하는 것이 좋으며, 이때는 `Exception` 클래스를 상속한다.
* `try/except` 안의 블록 코드양을 최소화하도록 한다.
* `finally`는 사용하는 것이 좋다; 자원 정리에 용이하기 떄문이다.
* 예외를 처리할 경우에는 쉼표 대신에 `as`를 사용한다.





