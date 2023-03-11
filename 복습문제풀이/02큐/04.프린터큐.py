# 프린터 큐 
# 중요도가 높은 순서대로 나간다! 
# 즉, 큐에서 먼저 나가는 건 중요도가 높은 순서야
# 그게 아니라면 다시 append돼야 해! 

# 1. 중요도가 같은 것들은 다 구분을 해줘야 돼! 
from collections import deque 

N = int(input())
queue = deque()
for i in range(N):
    # 3번 입력을 받는다. 
    count, order = map(int, input().split()) # 문서 개수 궁금한 문서 위치 
    documents = list(map(int, input().split()))

real = [[idx, value] for idx, value in enumerate(documents)]
    
for i in real:
    queue.append(i)

print(queue)

    