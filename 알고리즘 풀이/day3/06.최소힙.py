# 최소힙 구하기! 

#  10의 5제곱 이니까 Nlogn까지 풀 수 있음.

import heapq
import sys
heap = [] # 힙 구조 # 빈 배열(힙) 생성
N = int(input())
answer = ''
for i in range(N): # N만큼 반복 
    command = int(sys.stdin.readline().rstrip('\n')) # ❗️입력 값을 input으로 받았더니 시간복잡도 error남❗️
    # 연산은 무조건 양의 정수와 0만 올 수 있음
    if command == 0:
        if not heap:
            # 0인데 heap이 비어있다면 
            answer += '0' + '\n'
        else: # 가장 작은 값을 출력하고 빼준다.
            answer += str(heapq.heappop(heap)) + '\n'  
    else: 
        # 0이 아닌경우...! 즉, 양의 정수일 경우! 
        heapq.heappush(heap, command)


print(answer) # 반복문과 동일선상에 놓는다 = 반복문을 빠져나왔다.
# for i in range(4):
#     number = int(input()) # 숫자를 하나 입력을 받음..! 
#     heapq.heappush(heap, number)

# print(heap)

# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))

# print(heap)