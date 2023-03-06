N = int(input()) # 숫자만큼 입력을 받아...! 

stack = []
# 원래는 배열을 입력을 받아서.. 판단하는 함수를 만들어줘도 돼! 

for i in range(N):
    number = int(input()) # 숫자하나 입력을 받아..! 
    stack.append(number) if number != 0 else stack.pop()

if stack:
    print(sum(stack)) # 합을 구하고..! 
else:
    print(0)