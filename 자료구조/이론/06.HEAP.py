# 힙(자료구조) : 최댓값, 최솟값을 빠르게 찾기 위한 자료구조! 

# 부모노드의 자식이 자식노드의 값 보다 크거나(작거나) 같은 
# ❗️완전 이진트리 or 포화 이진트리❗️

# BST는 자식끼리도 분명 오른쪽 자식이 더 크다는 것을 알 수 있다. 
# 하지만 heap은 자식끼리는 비교할 수 없고, (❗️반 정렬 상태이다 => 자식끼리는 정렬이 안 됨❗️)
# 또한 공통된 노드가 들어올 수 있다.
# 파이썬으로 구현이 가능! 

# 힙 종류 
# 최대 힙 : 부모 노드가 자식 노드보다 무조건 같거나 큼 
# => ❗️ 루트 노드가 가장 큼 ❗️

# 최소 힙 : 부모 노드가 자식 노드보다 무조건 작거나 같음 
# => ❗️ 루트 노드가 가장 작음 ❗️


# heap은 최댓값, 최솟값을 빠르게 찾아내기 위해 고안된 자료구조! 
import heapq
# 최소힙을 지원한다! 

heap = [] # 빈 힙 생성 
# heap에 값 삽입 
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 130)
heapq.heappush(heap, 70)

print(heap)

# heap에서 값 삭제 
heapq.heappop(heap) # 최소 힙이니까 가장 작은 수 부터 나감 
print(heap) # 10이 제일 먼저 나감

# 리스트를 한 번에 heap으로 변환 
arr = [40,10,20,25,1,7,10] 
heap1 = []
# 최대 힙 구현 
for i in arr:
    heapq.heappush(heap1, i * -1)

print(heapq.heappop(heap1) * -1) # 이런식으로 넣을 때 -1을 곱하고 출력할 때 그 값에 -1을 곱하면 돼! 

# 즉, 가장 큰 값에 -를 씌우면 가장 작은 값이 바로 돼 버린다. 

