# 세 자리수 곱셈!! => 배열로 바꿔서 계산한다.
# a = 345
# b = str(a).split('')
# print(b, type(b))


# -1) list(문자열 or 문자열 변수)
# ❗️ 공백문자를 포함해서 배열로 갈라줌 ❗️
# ⭐️ 붙어있는 문자도 가능함! ✨

# -2) split() : 스페이스 기준이 default
# 파이썬에서 split으로 붙어있는 문자열 쪼개는 건 없는거같음.

# let str = "wdwdwdwdw";
# console.log(str.split("")) // js는 돼!
# name = "jisung"
# # arr = name.split("") ❗️ERROR❗️
# print(arr)

num1, num2 = input().split(' ')
arr = list(num2)

for i in range(len(num2), 0):
    print(int(num1) * int(num2[i]))
