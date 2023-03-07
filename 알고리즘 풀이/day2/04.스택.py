# 명령 
# push 값! 
stack = []
N = int(input()) # 14번 입력을 받는다..! 
answer = ''
for i in range(N):
    command = input().split()
    # split() : 파이썬의 배열은 동적이라 알아서 개수대로 만들어짐..! 
    if len(command) == 2: # push를 받을 때...! 
        stack.append(int(command[1])) # 숫자로 바꿔서 넣는다!! 
    else:
        if command[0] == 'top':
            if not stack:
                answer += '-1' + '\n'
            else:
                answer += str(stack[len(stack) - 1]) + '\n'
        elif command[0] == 'size':
            # print(len(stack)) # stack에 들어있는 정수의 개수
            answer += str(len(stack)) + '\n'
        elif command[0] == 'empty':
            if not stack: # 비어있다면 1 아니면 0
                answer += '1' + '\n'
            else:
                answer += '0' + '\n'

        elif command[0] == 'pop':
            # 비어있다면 -1출력 
            if not stack:
                answer += '-1' + '\n'
            else:
                answer += str(stack.pop()) + '\n'

print(answer)