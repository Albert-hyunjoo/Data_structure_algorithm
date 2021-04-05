# 파이썬 자료구조와 알고리즘
# 1.2 내장 시퀀스 타입
# ===========================

# 시퀀스 데이터 타입의 특징은?
# 1) 멤버십 연산 (IN, 포함여부)이 가능하다
# 2) 크기 함수 (len(seq) 사용이 가능하다
# 3) 시퀀스 데이터는 인덱싱이 되어있으므로 슬라이싱이 가능
# 4) 반복문을 통해서 데이터 순회가 가능하다

# 가변성에 대해서
# 1) 시퀀스 데이터 타입은 가변적이다. (추가/삭제 O)
# 2) 모든 변수는 객체 참조 (=)이므로, deep copy로 복사해야!
print("=====가변성의 예시=====")
a = [1,2,3,4]
a_copy = a[:]
a.remove(1)
print(a, "a에서 1제거")
print(a_copy, "a에서 1제거 -- 영향 없음")

# 슬라이싱에 대해서
# 1) 기본적인 문법은 시퀀스 데이터 [시작:끝:스텝]
print("=====슬라이싱의 예시=====")
a = [1,2,3,4]
print(a[0], "-- a의 첫번째")
print(a[1], "-- a의 두번째")
print(a[0:2], "-- a의 첫~세번째")
print(a[0:-1], "-- a의 맨뒤에서 앞에서 3번째")

# 시퀀싱의 종류 1: 문자열 (str)
# 1) 문자열은 일련의 문자인 시퀀싱 데이터 타입
# 2) 문자열은 다양한 메서드 (join, ljust, format)가 있음
print("=====문자열 메서드의 예시=====")
b = "1234 5678 9101112"
print(" ".join(b), "-- 공백을 연결자로 join 예시")
print("안녕하세요, {0}님. 환영합니다.".format("주현석"), "-- format의 예시")
print("*** 로컬 변수로 키와 딕셔너리 만드는 예시 ***")
key = 1 # 로컬 변수 1
value = "국어" # 로컬 변수 2
print("{key}:{value}".format(**locals()), "-- 로컬변수에서 맞는 형태의 format를 찾아 assign")
print("=====split의 예시=====")
c = "버피*크리스-메리*16"
print(c, "-- 원래 문자열")
print(c.split("*"), "-- * 기준으로 split")
print(c.split("-"), "-- '-' 기준으로 split")
print(c.split("*",1), "-- * 기준으로 앞의 1개 기준으로만 split")
print("=====strip의 예시=====")
d = "321예시의 문장321"
print(d, "-- 원래의 문장")
print(d.strip("321"), "-- 앞의 321 제거")

# 튜플 (Tuple) 에 대해서
# 1) 튜플은 ,로 구분된 값으로 이루어지는 '불변' seq
# 2) 튜플은 인덱싱 및 카운팅은 가능, 추가는 불가능하다.
# 3) 튜플의 언패킹을 통해서 분할 assign이 가능하다. (x, *y)

## 네임드 튜플 (namedtuple) 에 대해서
## 1) 네임드 튜플은 인덱싱을 이름으로 참조가 가능하다,
## 2) 첫번째 인수는 만들고자 하는 데이터 타입, 두번째는 항목
## ex) collections.namedtuple("person", 'name age gender')

# 리스트 (list) 에 대해서
# 1) array의 일종으로, 요소의 연속된 구조이다.
# 2) 직접 접근 (즉, 탐색) 에 유리하지만 (O(1)), 추가시 O(n)
# 3) 대신에 크기를 동적으로 조절할 수 있는 ADT (추상 데이터 타입) 이다.
# 4) append (단수), extend (다수), insert, remove, pop...
# 5) 리스트 컴프리헨션: [항목 for 항복 in 반복 객체 if 조건문...]

# 연습 문제 1 - 전체 반전
# 재귀를 활용해서 풀어본다면?
# revert(s) 함수는 s[-1] + revert[:-1]
print("=====연습 문제 1=====")
def revert(s):
    if len(s) < 2:
        return s
    else:
        return s[-1] + revert(s[:-1])
print(revert("abcd"), "-- 원래 문자열 : abcd")

# 연습 문제 2 - 단순 문자열 압축
# EX) "aaabbcca" => a3b2c2a1
# 계속 순회문을 돌면서 index를 기억해서
# 전과 다르면 result에 기록하고, count 기록후 reset

print("=====연습 문제 2=====")
def str_compression(s):
    count, last = 0, s[0]
    list_aux = []
    for chr in s: # aaabbccaaa
        if chr == last:
            count += 1
        else:
            list_aux.append(last)
            list_aux.append(str(count))
            count = 1
            last = chr
    list_aux.append(last)
    list_aux.append(str(count))
    return "".join(list_aux)

print(str_compression("aaabbccaaa"))













