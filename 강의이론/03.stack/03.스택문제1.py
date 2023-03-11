# n은 10의 5제곱이다. 
# ❗️n제곱으로 풀면 안 돼❗️
# 1. 직관적으로 생각하기 
# - 일단 완전 탐색으로 풀어봐 

# 근데 n^2으로 풀지말라며 => 완전탐색 말구 다른 방법으로 풀어봐,..! 
# 라는 뜻 

# 완전탐색으로 하는 것이 옳지 않다면 다른 자료구조 알고리즘을 생각해내야 한다. 


temperature = [73, 74, 75,71,69,72,76,73]
# stack의 원소 1개를 넣고 그 수를 찾아서 거기부터...! 

# 1. 반복문을 2번쓰지 말자...! 
# 2. 모든 수를 하나하나 비교할건데, 그 수를 기반으로 그 수보다 큰 게 나오면 바로 break
stack = []
for i in range(0, len(temperature)):
    stack.append(temperature[i])
    count = 0
    for j in range(i + 1, len(temperature)): # 무조건 N번 도는게 아니야...! 
        # i + 1부터...! 
        if temperature[j] > temperature[i]:
            # 보다 크면...! 
            stack.append(temperature[j])
            count += 1
            break # 이거 때문에 N번 돌지않아...! 
        else: # 작다면... 
            if j == len(temperature) - 1:
                # 계속 작은것만 나왔는데 마지막날 까지 안 나왔다면...
                # 튜플을 사용해서 하는 거...! 
                
                count = 0 # 없다고 알려준다. 
                break # 반복문 여기까지 해도 돼!! 
            else:
                count += 1
    print(i,"일", count)


# N^2은 for문이 무조건 n번 돌아야 해! 
# 하지만 이중 for문은 무조건 n번을 돌지 않아. 
