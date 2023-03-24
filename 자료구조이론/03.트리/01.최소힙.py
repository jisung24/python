# 백준 최소힙 
import heapq 
import sys # 여러 줄 입력받을 때..! 

N = int(input()) # 연산의 개수 9개 입력! 
heap = []

for i in range(N): # n번 반복..! 
    data = int(sys.stdin.readline().rstrip('\n')) # 정수 입력받음! 
    # int(input())으로 입력 받았는데 시간초과 뜸! 
    # sys.stdin.readline()으로 한 줄씩 입력받자! 
    if data > 0: # 자연수라면 
        heapq.heappush(heap, data) # 넣는다! 
    elif data == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)) # 뺀 값을 출력