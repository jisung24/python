# 1. 문제 이해 
# - 카드의 합이 21이 넘으면 안 돼! (((((카드 합 <= 21)))))

# - 카드에 쓰여져 있는 숫자들은 모두 양수이다. 

# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다...! 

# N장 중에 3장을 선택해서 3장의 합 <= M이 되는 가장 최댓값을 구해라..! 
N, M = list(map(int, input().split(' '))) # 파이썬 판 배열 구조분해할당! 
cardList = list(map(int, input().split())) # 스플릿 아무것도 없으면 띄어쓰기 기준!! 

answer = []
for i in range(0, len(cardList)):
    for j in range(i+1, len(cardList)):
        for k in range(j + 1, len(cardList)):
            # 다 넣지말고... 조건을 걸어서 넣어줘...! 
            sumOfCard = cardList[i] + cardList[j] + cardList[k]
            if sumOfCard <= M: # 무작정 다 append떄리지 말고.. 
                # 배열을 넣을 떄 미리 조건을 따지고 넣자!
                answer.append(sumOfCard)


print(max(answer))