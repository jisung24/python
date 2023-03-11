# 입력 형태 
# 6
# 3 4 2 12 6 8
import heapq
import sys
N = int(input())
# 문제에서의 maxValue는 2보단 무조건 크다. 
numlist = list(map(int, input().split())) # numlist 입력받음..! 
# 최대힙으로 최댓값 구함. 
maxValue = max(numlist) # 잘 찍힘..! 
# 2보단 무조건 큼 
# N을 구하는 방법 
# N은 A가 아님 => 최소 2로 곱해야 돼..! 
# 곱했을 때 숫자들이 다 나눠지면 그 수가 정답.! 

i = 2
while True:
    maxValue *= i # maxValue를 변경시켜줌..

    for num in numlist:
        if maxValue % num != 0:
            # 나눠지지 않는경우! 
            i += 1
            break
    
    # 나눠 진다는 소리야...! 
    # print(i, "로 나누면 돼!")
    break

print(maxValue)
