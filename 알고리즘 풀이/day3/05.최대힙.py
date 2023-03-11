import heapq
import sys

N = int(input())
heap = []
# 최대힙은 그냥 -로 거꾸로 출력해주면 돼..! 
answer = ''
for i in range(N):
    command = int(sys.stdin.readline().rstrip('\n'))

    if command == 0:
        if not heap:
            answer += '0' + '\n'
        else:
            # 값이 있는 경우...! 
            answer += str((heapq.heappop(heap)) * -1) + '\n'
    else:
        # 자연수일 경우..! 
        heapq.heappush(heap, command * -1)

print(answer)



