from collections import deque
arr = [1,2,3]
queue = deque(arr) 


# enqueue(값 넣기)
queue.append(4)
print(queue)

# extend (한 번에 여러 값 넣기)
queue.extend([5,6,7])
print(queue)

# dequeue 
queue.popleft()
queue.popleft()
queue.popleft() # 맨 앞 원소 3개 pop! O(1)로!
print(queue)

# ❗️ rotate 중요 ❗️
# 빼고 자기차례 아니면 다시 들어오는 거! 
queue.rotate(-1) # 1번 
queue.rotate(-2) # 2번  =>  총 3번!
# rotate(-큐 길이)하면 원래대로 돌아옴! 
# 그래서 while문으로 rotate(-1)하면 조건이 될 때 까지 계속 나갔다 들어왔다를 반복한다. 
print(queue)