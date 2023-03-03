def solution(n):
    # 피자 1판 당 7조각인데, n명이 최소 1개 이상은 먹어야 한다.
    # 15명이면 적어도 7 * 3조각은 있어야 돼..! 
    # 그니까 7을 계속 곱해서 조각을 넘어서는 순간 그 순간이 값이야! 
    i = 1
    while True:
        if  7 * i < n:
            i += 1
        else: # 크거나 같아졌어! 
            break

    answer = i
    return answer

