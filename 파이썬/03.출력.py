# print함수 출력

# 1. 일반 print + 변수
name = "jisung"
# print("Hello, World! %s", name)
# print("Hellow World", end="%%")  # 끝 문자를 바꿔줌 ( 원래는 다음줄로 자동으로 넘어가는 거! )
# print("Hellow World", end=" ")
# print("Hellow World", end=" ")

# print는 원래 콤마로 구분자를 지어서 출력해준다.
print("one", "two", "three")

# ❗️2. sep=""(구분자 문자 변경)❗️
print("One", "Two", "Three", sep="-", end=" ")
print("=====Me======")

# ❗️3. end=""(줄바꿈 문자 변경)❗️
print('안녕하세요!')  # 이렇게 써주면 default로 \n이 들어감
print('제 이름은 >> ', end="# ")
print('제 이름은 >> ')

# ✨4. 변수를 이용한 출력
# -1) ⭐️ 콤마 뒤에 변수 적어주기 ⭐️
age = 25
a, b = 1, 2
print(type(age))  # type출력!
print('제 나이는 >> ', age, end="끝\n")
print('제 나이는 >> ', age, end="끝\n")

# -2) ⭐️ format ⭐️
# - 문자열 안에 {}를 넣어주고 .format(변수)를 사용해주면 돼!
print("제 나이는 - {}살".format(age), end="끝\n")
print("a >> {},b >> {}".format(a, b))

# -3) ⭐️ f + {변수} ⭐️
print(f"출력할 a = {a}, b = {b}")
print(f"a = {a}, b = {b}")

# -4) 소수점 출력하기 ⭐️ format함수⭐️
c = 13.3444444
print(format(c, "1.3f"))  # 뒷자리 세 번째 자리까지 출력!


# -5) +를 이용한 변수출력
d = "dwdawdawd"
print("+를 이용한 변수출력 >> " + d)


# format + {}를 주로 사용하자!
e = "seoul"
f = "jeju"
print(f"e >> {e}, f >> {f}")
