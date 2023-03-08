import sys
from collections import deque

queue = deque([]) # 빈 큐 생성하고 시작함..! 
N = int(input()) # 숫자 하나 입력받음.. => 이 만큼 반복해준다.
answer = ''

for i in range(N):
    command = sys.stdin.readline().split() # 둘 다 문자열 띄어쓰기 기준으로 입력받음..! 

    if command[0] == 'push':
        # push 일 경우..! 
        queue.append(int(command[1]))

    if command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft() # 가장 앞에 있는 원소...! 

    if command[0] == 'size':
        print(len(queue))
        # 큐에는 무슨 짓 안 해도 돼! 
    if command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    if command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])


# print쓰는 게 값 일일이 형번환 해서 answer에 넣고 출력하는 거 보다 훨씬 가벼움..!  
# str 은 로그 N






# q = deque([])
# print(not q) # queue가 비어있는지..! 
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# print(q)
# print(not q) # queue
# print(q[-1]) # 마지막 원소! 