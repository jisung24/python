# 제로! 

# ❗️ 0이 나온다면 제거할 수가 나옴을 보장한다 ❗️
# 그럼 스택이 비어있다면 0이 안 나옴

stack = []
N = int(input()) # 4를 입력받음

for i in range(N):
    number = int(input())
    if not stack:
        # 비어있을 땐 어차피 0이 안 들어오니까...
        stack.append(number)
    else: # 안 비어있다면..
        if number != 0:
            stack.append(number)
        else:
            stack.pop()

print(sum(stack))
