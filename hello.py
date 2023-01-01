# 파이썬 기초문법 정리!

# 1. 자료형 ==> type(변수) : 어떤 타입인지 검사!
# - ❗️숫자형❗️
# -1) 정수(int) : (1, -2, 2)
# -2) 실수 : (1.677, -35.55);
# -3) 컴퓨터식 지수 표현 방식 (4.24e10) ❗️거의 쓸 일 없음.❗️(float)
# -4) 8진수 (0o77)(int)
# -5) 16진수 (0x7d)(int)
# =========> 정수 실수만 쓰이고 3,4,5는 거의 쓸 일 없음.
print(type(1))  # int(정수)
print(type(3.444))  # float(실수)
print(type(2.42e10))  # float
print(type(0xffdf))  # int
print(type(0o77))  # int
print(type('Hello World'))  # str(문자열)
# - 문자(str type)
print(type('c'))  # str
print(type('Eh'))  # str
# 문자열 사용 방법
print("안녕! 내 이름은 \'김지성\'이야!")

# - 불(대문자로 작성해줘야 함.)
print(type(True))  # bool
print(type(False))  # bool
# - 변수
# - 리스트
# - 튜플
# - 딕셔너리
# - 집합


# 연산자!!
print(3 + 4)  # 덧셈 연산자
print(3 * 4)  # 곱셈 연산자
print(3 - 4)  # 뺄셈 연산자
print(3 / 2)  # 1.5 (소수점까지 나옴)
print(3 // 2)  # 몫 연산자(정수만 나옴)
print(5 % 3)  # 나머지 연산자
print(3 ** 2)  # 제곱 연산자
