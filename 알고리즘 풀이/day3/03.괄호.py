# 내가 deque를 전역으로 받아줘서 그래...............................
N = int(input())
def isTrue(data):
    stack = [] # 각각 따로 검사니까 여기다가 지역변수로 입력을 받아줘야지...! 
    
    for i in data:
        if i == "(":
            stack.append(i)
        else: # 닫는 괄호..! 
            if not stack:
                return "NO"
            else:
                stack.pop() # stack을 pop

    # 반복문 빠져나와서.. => 반복문이랑 동일한 위치에 적어주면 돼! 
    if not stack:
        return "YES"
    else:
        return "NO"


answer = []

for i in range(N):
    data = input() # 괄호를 입력을 받음...! 
    answer.append(isTrue(data))

print('\n'.join(answer))
