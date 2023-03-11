# 일단 4byte당 long을 하나씩 증가시켜준다! 

cnt = int(input())
answer = ''
for i in range(1, cnt // 4 + 1):
    answer += "long "

print(answer+'int')
