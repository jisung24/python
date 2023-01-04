year = int(input())

# if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#     print("1")
# else:
#     print("0")

# 이런 간단한 이거아니면 저거~ 라는 조건은 삼항연산자를 사용해주면 편하다.

print("1") if (year % 4 == 0) and (year %
                                   100 != 0 or year % 400 == 0) else print("0")

# 파이썬 삼항연산자 이론
# 참 값 if 조건 else 거짓 값
# 즉 참이면 if앞 왼쪽에! 거짓이면 else 뒤 오른쪽에!
