# 스택 그냥 사용하면 돼! 
# sys.stdin.readline() => '\n'까지 입력을 받아준다. => 자동으로! 
stack = []

# append, pop조건을 따로 설정해주면 돼! 
n = int(input()) # 정수 1개! 
i = 1;
answer = []
for i in range(0, n):
    number = int(input()) # 숫자 하나 한 줄로 입력 받음! 
    # i가 number가 될 때 까지 stack에 넣는다.
    while i <= number: # 내가 계속 ()를 쳐줘서 틀렸음..
        stack.append(i)
        answer.append('+')
        i += 1

    # push는 안 해! 
    # 이제 number보다 i가 큼! 
    if number == stack[-1]:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit(0)

print('\n'.join(answer))

