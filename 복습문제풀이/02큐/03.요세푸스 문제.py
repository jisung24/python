# 순서대로 사람을 제거 => 순서대로 큐이다! 
from collections import deque 

queue = deque()
N, repeat = map(int, input().split())
answer = []

# O(N)
for i in range(1, N + 1):
    queue.append(i)

# 큐를 싹 채워주고 시작한다. 

while len(queue) != 0:
    # 0이 아닐 때 까지...! 
    print(queue)
    for i in range(0, repeat):
        if i != repeat - 1:
            queue.append(queue.popleft())
        else:
            answer.append(str(queue.popleft()))

    # 3번 다 돌았어...! 
    # 이걸 계속 queue가 없어질 때 까지..! 

print("<",", ".join(answer)[:],">", sep='')