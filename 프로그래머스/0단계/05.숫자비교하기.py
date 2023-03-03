# num1 num2가 같으면 1 다르면 -1 

# 삼항 연산
# print("even") if a % 2 == 0 else print("odd")
def solution(num1, num2):
    answer = 1 if num1 == num2 else -1
    return answer