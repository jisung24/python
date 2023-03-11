# 순서대로 먼저 나간다! 

from collections import deque 

N = int(input())
queue = deque()

# O(N)
for i in range(1, N + 1):
    queue.append(i)

# 큐에 값을 채워넣고 이제 돌리는거야..! 
# popleft
# append(popleft) 를 하고나서... 

while len(queue) != 1:
    # 1. popleft
    queue.popleft()

    # 2. 다시 집어넣기
    if len(queue) == 1:
        break
    # 보면 popleft하고 1개 남았을 때! 
    # 굳이 append popleft 안 해도 돼!!! 
    # 마지막 줄은 len큐가 1이 아닐 때 만 해도 되는 연산이야..! 
    # 발전하고 있어...! 
    queue.append(queue.popleft()) 

print(queue[0])


# 반복문 안에서 해야 할 일은 2가지 
# 근데 1개가 끝나고도 체크를 해줘야 할 게 있음 
# 그럼 그냥 1개 끝나도 나갈 수 있게끔 break걸어주면 돼! 
