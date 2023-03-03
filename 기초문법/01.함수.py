def add(num1, num2):
    return num1 + num2

print(add(1,2))


# 자바스크립트 배열 구조분해 할당에선 
# 배열을 2개로 나누려면 [a, b]를 적어줬지만 
# 파이썬은 그냥 a, b라고 적어주면 배열이 나뉜다. 

# ❗️백준 연습문제 1000❗️
num1, num2 = input("").split(' ') # 문자열을 입력받는 함수 input 

print(add(int(num1), int(num2)))