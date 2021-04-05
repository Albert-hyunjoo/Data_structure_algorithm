# 파이썬 자료구조와 알고리즘
# 1.1 Integer (정수)
# ===========================

# 정수의 특징은 무엇인가?
# 1) 정수는 불변형으로 작용하고
# 2) 크기는 메모리에 의해 제한된다 (32 >)
## 단, 파이썬 정수 크기는 (정수).bit_length()로 풀 수 있다.
# 3) 정수는 기본 10진법, 다른 진법으로 변환하려면 int(문자열, 밑) 으로 표현할 수 있다.
## 예시 코드에 대해서
print("=====int=====")
s = "11"
d = int(s)
print(d) # d는 11 (10진법)
e = int(s, 2)
print(e) # 이진법 기준으로 11이면 2*0 + 2*1, 즉 e는 3 (2진법)

# 정수 및 부동 소수점 관련 메서드
# 1) divmod(x, y) = 몫과 나머지를 튜플 형태로 return
# 예시의 코드 (divmod)
print("=====divmod=====")
print(divmod(45, 6))# 몫이 7, 나머지 3 (7,3)

# 2) round(x, n) = n이 음수인 경우에는 x를 n만큼, n이 양수면 x를 소수점 이하
# 3) as_intger_ratio() = float을 분수로 표현한다 (2.75 -> 11/4)
print("=====as_integer_ratio=====")
print(2.75.as_integer_ratio())

# 복소수에 대해서
# 1) 복소수는 부동소수점 한 쌍 갖는 불변형이다.
# 2) 복소수는 cmath 모듈 임포트 후에 사용이 가능하다.

# 분수를 다루는 fraction 모델
# 1) Fraction 모듈 통해 분수 값을 리턴한다 (분자, 분모)
# 예시 코드에 대해서 (Fraction)
print("=====Fraction Method=====")
from fractions import Fraction
def rounding_floats(number1, places): # float을 반올림
    return round(number1, places)
def float_to_fractions(number): # float을 분수로
    return Fraction(*number.as_integer_ratio()) # 분수로 2개가 오므로, * (다중 input) 로 설정
print(float_to_fractions(1.25))

# decimal 모듈
# 1) 10진법 부동소숫자는 decimal.Decimal(정수)을 활용한다
# 2) decimal 모듈에는 exp(x) 등의 내장함수가 있어 사용이 가능하다.
# 3) 정확도가 필요한 경우에는 이 모듈을 적극적으로 활용한다

# 진법 변환 연습문제는?
# final) convert_to_decimal(원래, 진법) = 원래 숫자를 10진법으로
# 전반적인 알고리즘을 짜보기
## ex) 차근차근 해보기 (1111, 2)
## 1) 1111에서 1을 extract?
## 1-1) 원래 번호의 /10 나머지에 더하면 1
## 2) 1 * base를 곱해서
## 3) result에 더하고, 이를 반복
# 어떤 숫자를 나누고, 그 나눈 자리수로 곱해서 더하는 것
def convert_to_decimal(number, base):
    result = 0
    multiplier = 1
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base # 거듭제곱의 효과
        number = number // 10
    return result

if __name__ == "__main__":
    print("=====진수 바꿔서 십진수로=====")
    print(convert_to_decimal(1111, 2))
    print(convert_to_decimal(1111, 3))

# 최대 공약수 구하는 연습문제는?
# final) gcd(a,b) = ?
# 최대공약수 구하는 공식 중, gcd(a,b) = gcd(b, a%b)
# 즉, a와 b의 최대공약수는 b, a%b의 최대공약수와 같다.

def gcd(a,b):
    while (b!=0):
        result = b
        a, b = b, a%b
    return result

if __name__ == "__main__":
    print("=====최대 공약수 구하는 공식=====")
    print(gcd(12, 21))
    print(gcd(21, 12))
    print(gcd(3, 15))
    print(gcd(3, 26))

# 소수 구하는 연습 문제는?
# final) finding_prime_sqrt(number) == True or False
# 즉, 소수가 아니면 False, 소수면 True
# 소수의 brute Force 대신 제곱근을 이용한다고 가정하면,
# m*m = n으로 가정할 때, n이 소수가 아니면 n = a*b, 즉 m*m = a*b
# 즉, m까지 살펴보고 없으면 소수가 맞다 (m는 여기서 찾고자 하는 숫자의 제곱근)
import math

def finding_prime_sqrt(number):
    num = abs(number) # 혹시 소수가 들어갈 수 있으므로
    if num < 4: return True # 1~3까지는 왠만하면 소수
    else:
        for x in range(2, int(math.sqrt(num)) + 1):
            if number % x == 0:
                print("divided number:", x)
                return False
    print("No divided Number!")
    return True

if __name__ == "__main__":
    print("=====소수를 구하는 경우=====")
    print(finding_prime_sqrt(16))
    print(finding_prime_sqrt(15))
    print(finding_prime_sqrt(13))
    print(finding_prime_sqrt(533))
    print(finding_prime_sqrt(997))