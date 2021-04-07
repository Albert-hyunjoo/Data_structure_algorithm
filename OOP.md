# 객체지향 설계 (OOP)

## 클래스와 객체

* 객체를 만들 때에는 **객체의 유효성 여부**를 체크! 즉 우리가 원하는 형태의 객체를 만들 수 있어야 한다.
* 이는 데이터의 **패키지화와 메서드**를 통해 실현이 가능하다.
* **클래스**는 **사전에 정의된 특별한 데이터와 메서드의 집합**, 이를 통해 만들어진 실체를 **객체**라고 한다.
* 객체가 소프트웨어가 실체화되어 올라갈 때에는 이를 **인스턴스**라고 한다.

### 클래스 인스턴스의 생성
* 클래스 인스턴스는 함수 표기법을 통해 **초기 상태의 객체**를 생성한다.
* 생성자 (constructor) 를 통해서 `__new__` 메서드가 호출되어 할당, `__init__`이 초기화

#### 인스턴스의 구성 요소 1 | 속성 (attribute)
* 객체에는 데이터와 메서드로 구성된 클래스 "속성"이 존재한다.
* 메서드 속성은 통상적으로 함수로 구성되며, 첫번째 인수는 인스턴스 (self)

#### 인스턴스의 구성 요소 2 | 네임스페이스 (namespace)
* 객체로 매핑해서 파이썬 딕셔너리 형태로 구현한다.
* 네임스페이스의 예로는 **내장된 셋, 모듈의 전역 이름, 함수의 전역 이름**으로 구성
* 스크립트 파일의 최상위 호출에 실행되면, `__main__`모듈의 일부로 실행되어, 고유의 스페이스

#### 인스턴스의 구성 요소 3 | 스코프 (Scope)
* 네임 스페이스에 직접 접근 가능한 파이썬 프로그램의 텍스트 영역

## 객체지향 프로그래밍의 원리

### 특수화
* 슈퍼 클래스의 모든 속성을 상속하며, 재정의 (override) 될 수 있다
* 만약 상속받지 않으면, 원칙적으로 `object`를 명시하는 것을 권장한다.

### 다형성
* 메서드가 서브 클래스 내에서 `override`될 수 있음을 말한다.
* `super()`를 통해서 상속 클래스의 필요한 메서드를 쉽게 호출할 수 있다.

### 합성과 집합화
* 합성은 한 클래스에서 다른 클래스의 인스턴스 변수를 포함 (클래스의 관계)
* 파이썬의 모든 클래스는 상속을 사용한다 (상위의 클래스 `object`에서)

# 디자인 패턴

* 디자인 패턴은 잘 설계된 구조의 형식적 정의를 소프트웨어 엔지니어링으로 따로 옮긴 것
* 여러가지 문제를 각기 다른 디자인 패턴을 통해 해결할 수 있다.

## 데코레이터 패턴
* 데코레이터 패턴은 @표기를 통해서 함수 또는 메서드의 변환을 지정해주는 도구
* 주로 원래 있던 코드에 래핑을 통해서 굳이 코드를 바꾸지 않아도 원하는 형태로 바꾸도록

### 데코레이터의 예시 (Date-Time 추가) 
아래 코드의 출처는 [ㅍㅍㅋㄷ](https://bluese05.tistory.com/30) 이다.    

#### 1) 가장 기본적인 코드 형식
```python
# 가장 기본적인 코드 형식
def main_function():
    print("MAIN FUNCTION START")
```

#### 2) 여기서 추가하고자 하는 코드 (기능) – 출력 당시의 날짜, 시간
```python
import datetime
def main_function():
    print(datetime.datetime.now())
    print("MAIN FUNCTION START")
    print(datetime.datetime.now())
```
만약 추가 기능을 다른 기능에도 구현하고자 하는데, 그 기능이 100개~1000개 가까이 된다면 일일이 붙이는 것이 비효율적이다.

#### 3) 데코레이터 생성
```python
import datetime
def datetime_decorator(func): # wrapp하고자 하는 메인 function을 인수로 받음
    def decorated():
        print(datetime.datetime.now()) # 클로져 형식 (안에 내부 함수 정의하고, 외부로 return)
        func()
        print(datetime.datetime.now())
    return decorated
# datetime_decorator(func)이 지나면,
# 안의 decorated()를 거쳐서 위아래의 print가 코드에 붙고
# decorated 전체가 return되므로, 코드가 정상적으로 실행됨

@datetime_decorator
def main_function_1():
    print("MAIN FUNCTION 1 START")
```

#### 4) 클래스 데코레이터 생성
* 클래스 데코레이터는 `__call__` 함수로 정의하는게 깔끔하다.
```python
import datetime
class datetime_decorator: # wrapp하고자 하는 메인 function을 인수로 받음
    def __init__(self, f):
        self.func = f # 기본적으로 function이 들어가야 한다.
    
    def __call__(self, *args, **kwargs): # 함수를 정의하는 일반적 변수
        print(datetime.datetime.now())
        self.func(*args, **kwargs) # 뭐가 들어오든 받는다.
        print(datetime.datetime.now())

class MainClass:
    @Datetime_decorator
    def main_function_1():
        print("MAIN FUNCTION 1 START")
```
### 데코레이터의 `@staticmethod`와 `@classmethod`
* 둘의 공통점은 일단 인스턴스를 굳이 만들지 않아도 `class`의 메서드 실행이 가능하다.
* 단 `@staticmethod`는 클래스 안의 속성 등을 사용할 때, 정적으로 접근해야 한다.
* `@classmethod`는 중간에 `cls`를 인수로 받으므로 클래스의 속성에 접근이 쉽다.
* 만약 클래스 내의 속성이 숨겨져 있으면 (변수) `@classmethod`가 낫다.

#### 예시 코드 (정적 <-> 클래스)
```python
class A(object):
    _hello = True # 숨겨져 있다.
    
    def foo(self, x):
        print("foo {0}, {1} 실행".format(self, x))
        
    @classmethod
    def class_foo(cls, x):
        # 인스턴스 안만들어도 A의 _hello에 접근
        print("class_foo({0}, {1} 실행".format(cls, x, cls._hello))

    @staticmethod
    def static_foo(x):
        # 인스턴스 안만들어도 A의 _hello에 접근
        print("static_foo({0}) 실행".format(x))

if __name__ == '__main__':
    a = A() # 인스턴스 a 생성 (from A 클래스)
    a.foo(1) # a 객체의 attr인 foo를 실행해서 "(foo a객체, 1) 실행"
    a.class_foo(2) # 객체의 cls 메소드므로, @classmethod식으로 cls를 받아서 foo_class(A,2) 실행
    A.class_foo(2) # 클래스에서 접근했다 -- 그러므로 위의 인스턴스 접근 결과와 같음
    a.static_foo(3) # staticmethod에서 접근
    A.static_foo(3) # 똑같이 나옴
```

### 옵저버 패턴 (observer)
* 특정 값을 유지하는 핵심 객체를 갖고, 객체의 일대 다 관계에서 효과적으로 내용 변경
* 옵저버는 통상적으로 `property`로 구현하며, 이 데코레이터로 속성의 특성을 제어한다.

#### 예시 코드 (옵저버)
```python
class C:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name # name을 숨긴다.
    @name.setter
    def name(self, new_name): # 인스턴스.속성 형식으로 값 저장
        self._name = "{0} >> {1}".format(self._name, new_name)

c = C("진")
c._name # "진"
c.name # property의 name 메서드 사용 (진)
c.name = "아스틴"
c.name # "진" >> "아스틴"
```
### 싱글턴 패턴 (singleton)

* 초기화된 인스턴스의 전역 사용은 싱글턴 패턴을 사용한다.
* 왜? 파이썬에는 `private` 접근자가 없으므로, 중복 생성을 방지하려면 이 패턴을 사용해야 하므로
* 클래스의 `__new__` 클래스 메서드에서 이를 구현해야 한다.

#### `__new__`를 활용한 싱글톤 구현
```python
class SinEx:
    _sing = None # 숨겨져 있음
    
    def __new__(self, *args, **kwargs):
        if not self._sing: # 싱글톤이 없으면, 즉 객체가 없으면
            # self._sing은 SinEx 클래스에서 자기를 상속해서 집어넣는다. 
            self._sing = super(SinEx, self).__new__(self, *args, **kwargs)
        return self._sing # 있으면은 return

x = SinEx()
y= SinEx()
x == y # True     
```