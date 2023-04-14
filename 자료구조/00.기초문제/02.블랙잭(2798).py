# 조합 사용! 
from itertools import combinations
N, M = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

combine_result = list(combinations(cards, 3)) # 5 C 3 

answer = []

for i in range(0, len(combine_result)):
    total = sum(combine_result[i])
    if total <= M:
        answer.append(total)


print(answer[-1])