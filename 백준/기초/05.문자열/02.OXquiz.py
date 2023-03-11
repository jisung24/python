import sys
N = int(sys.stdin.readline().rstrip('\n')) # 정수 하나를 입력받음 
answer = []
for i in range(1, N + 1):
    # 1 2 3 4 5번 이렇게 입력을 받음... 
    result = list(sys.stdin.readline()) # 배열로 받아줌
    sum = 0
    added = 0
    for j in result:
        if j == 'O':
            added += 1 # 2점이 돼서 sum에 더해진다...
            sum += added # 
        else:
             added = 0
             sum += added
    answer.append(sum)

print('\n'.join(map(str, answer)))
# ❗️맞음❗️

# ❗️ stack을 사용해서 풀 수 있을 거 같아 ❗️

