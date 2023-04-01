# 그니까 stack에서 push pop을 이용해서 저 수열을 만들어야 돼! 
# push를 하는 순서는 반드시 오름차순을 지켜야 돼! 

# 만약 만들고싶은 수열이 4다? 
# 그럼 스택에서 1 2 3 4까지 넣고 4일 때 pop을 하는거지..! 
import sys
N = int(input()) # 정수하나 입력받음 
now = 1
stack = []
answer = []
for i in range(N):
    number = int(input())
    # 숫자를 입력을 받음...! 
    # 스택에 push를 하는 조건..! 
    # now가 number가 될 때 까지..! 
    while now <= number:
        stack.append(now)
        now += 1
        answer.append('+')

    # 다 넣었음..! 
    if stack[-1] == now:
        stack.pop()
        answer.append('-')
    else:
        print(-1)
        exit(0)
    

# 초심 잃지 말기!! 
# stack은 push pop조건만 제대로 설계해주면 돼! 