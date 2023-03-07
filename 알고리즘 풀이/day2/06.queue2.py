# 우선 큐 모듈을 사용하지 않고 그냥 있는 그대로 구현 
# ❗️무조건 dequeue 모듈로 구현해야 함❗️
# pop(0) 할 때 시간초과 무조건 나게 됨 
from collections import deque

import sys
n = int(input())
deq = deque()
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        deq.append(command[1])
    elif command[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])