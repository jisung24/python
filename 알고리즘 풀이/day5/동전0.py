N, total = map(int,input().split())
# N과 total입력받음..! 

typeOfMoney = []
for i in range(N):
    m = int(input())
    typeOfMoney.append(m)

typeMoney = sorted(typeOfMoney, reverse=True)
# 내림차순으로 입력받아줌...! 
totalCnt = 0

for i in typeMoney:
    count = 0
    if i > total:
        continue
    else:
        count = (total // i)
        total -= i * count
        # print("남은 돈 >> ", total, "개수 >> ",count)
        totalCnt += count

print(totalCnt)
