# 큐 구현 법 
# 👉 Array List(파이썬에서의 list)를 사용해서 구현 
# 👉 Linked List를 사용해서 구현 

# 근데 우리가 큐를 사용하고 싶을 때 마다 queue를 만들 순 없어 
# 파이썬에서 제공하는 deque library사용한다. 

# 큐 
# 먼저 들어온 data가 먼저 나가는 FIFO형식으로 데이터를 저장하는 자료구조 
# enqueue 👉 queue의 rear에 data를 추가 
# dequeue 👉 queue의 front에서 data를 꺼낸다

# ❗️큐를 array list를 사용하여 구현했을 때 dequeue 할 때 O(N)이 나서 별로 좋지 않음. 
# 🔴 그래서 우리는 linked list를 기반으로 큐를 구현할건데.....
# ✨ 파이썬에서 제공 된 deque(덱)이라는 linked list기반의 큐가 있어!!! 


# deque의 정의 
# 양 방향에서 enqueue dequeue가 가능한 자료구조 
# 즉, 양방향 큐라고 생각하면 된다! 
# 그래서 stack queue를 둘 다 구현할 수 있다. 
# ❗️list는 dequeue할 때 O(N)이 소요된다. 하지만 deque(덱)은 O(1)이 소요된다. 
# ❗️파이썬에서의 list는 array list인데 이건 느려서 deque덱은 linked list로 구현된다.

from collections import deque
queue = deque()

# rear에 값 삽입 
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# front에서 값을 꺼냄 (왼쪽으로 값 나감)
# front의 위치를 옆으로 옮겨주면 되기 때문에, 그냥 O(1)로 끝남
queue.popleft() # 제일 앞에 있는 값이 나감..! 

# 큐의 길이
print(len(queue))


# ❗️큐는 절대 코테에서 단독으로 구현되게 나오지 않는다❗️
# 다른 알고리즘을 구현하는 데 쓰임 ex) bfs bfs bfs bfs bfs bfs bfs bfs bfs›
