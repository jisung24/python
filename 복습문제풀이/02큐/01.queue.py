from collections import deque

N = int(input()) # 15

queue = deque() # 빈 큐 생성!
answer = ''
for i in range(N):
    command = input().split()

    if len(command) == 2: # push 일 때..! 
        queue.append(command[1]) # 어차피 answer에서 문자열로 출력..! 
    
    else: # 1일 때..! 
        if command[0] == 'pop':
            if not queue:
                # print(-1)
                answer += '-1' + '\n'
            else:
                print(queue[0])
                queue.popleft() # 앞에 있는 원소를 뺀다/
        
        elif command[0] == 'size':
            print(len(queue))

        elif command[0] == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif command[0] == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1]) 


# print문을 전부 str써서 answer로 바꿔줬더니 성공함! 
# print문 쓸 바엔 그냥 answer += str()쓰자!