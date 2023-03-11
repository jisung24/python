import sys 
from collections import deque 

N = int(input()) # N만큼 밑에서 반복할거야..! 
queue = deque([])
answer = ''
# 아까 봤듯이 print 10번 보다 그냥 형변환 + answer가 훨씬 빨라...! 

for i in range(N):
    command = sys.stdin.readline().rstrip('\n').split()
    # \n까지 받는데 저거 제외하고... split한다 

    if len(command) == 2:
        queue.append(command[1]) # 어차피 문자열로 들어가도 돼! 
        # 연산을 하거나 그런게 아니어서... 
    else:
        # 길이가 1 
        if command[0] == "pop":
            if not queue:
                answer += '-1' + '\n'
            else:
                answer += str(queue.popleft()) + '\n'
        elif command[0] == 'size':
            answer += str(len(queue)) + '\n'

        elif command[0] == "empty":
            if not queue:
                answer += "1" + '\n'
            else:
                answer += "0" + '\n'
        elif command[0] == "front":
            if not queue:
                answer += '-1' + '\n'
            else:
                answer += str(queue[0]) + '\n'

        elif command[0] == "back":
            if not queue:
                answer += '-1' + '\n'
            else:
                answer += str(queue[-1]) + '\n'

print(answer) 

# 이건 근데 또 print네...