# 배열 
from collections import deque 

queue = deque()

queue.append(120)
queue.append(150)
queue.append(180)
queue.append(80)
queue.append(50)

print(queue)

count = 0
while queue[0] >= 100:
    queue.popleft()
    count += 1


print(queue, count)