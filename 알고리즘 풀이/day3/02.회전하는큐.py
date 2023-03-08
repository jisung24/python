from collections import deque


queue = deque([])

queue.append(1)
queue.append(1)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

# 1번 연산 => popleft()
# 2번 

# queue.append(queue.popleft())
# print(queue)

# 3번 
# 맨 뒤에 값이 맨 앞으로 옴 
queue.appendleft(queue.pop())
print(queue)