
# 큐 
# 가장 먼저 들어간 data가 가장 먼저 나오는 요소 
# os에서도 상당히 많이 사용된다 

# 3가지만 알면 돼! 
# 1. 큐 구조 
# - 먼저 들어온 값이 먼저 나간다 (새치기 불가능하다)

# 2. 큐 용어 
# - enqueue : 큐에 원소를 삽입한다. 
# - dequeue : 큐에서 원소를 내보낸다 (가장 먼저 들어온 요소)
# - peek : 큐에서 가장 앞에 있는 원소, 즉, 먼저 나갈 예정인 요소 


# 3. 큐 관련 라이브러리 : deque

from collections import deque
arr = [1,2,3]
queue = deque(arr) # list에 있는 값을 큐에 넣어준다

# 1. enqueue : append로 구현한다.(1개 밖에 넣지 못 함)
queue.append(4)
queue.append(5)

# 2. extend : 한 번에 여러 개 넣기
queue.extend([8,9,100])
print(queue)

# 3. dequeue : popleft
# list로 구현하면 dequeue에서 시간복잡도 O(N)
# 따라서 연결리스트로 빼야하는데, deque가 연결리스트로 큐를 구현한 것! 
# 그래서 popleft를 이용하면 O(1)로 뺄 수 있음 pop(0)쓰지 마! 

queue.popleft()
print(queue)


queue.rotate(-3) # 뺸 순서대로 뒤로가서 쌓임 => 이거 매우 중요! 
print(queue)


# 다양한 정책의 라이브러리
# Queue() : 가장 일반적인 queue 
# LifoQueue() : stack 
# PriorityQueue() : 우선순위 큐

