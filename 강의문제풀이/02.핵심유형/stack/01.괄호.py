# 괄호 짝을 찾는 문제 
N = int(input()) # 정수 1개를 입력받음! 
# 함수형으로 짜볼게...! 
def solution(bracket):
    # 괄호가 들어오면... 출력해주는 함수!! 
    stack = []
    for i in bracket:
        if i == "(":
            stack.append("(")
        else: # i가 닫는 괄호일 때...! 
            if not stack: # 스택이 비어있다면..
                return "NO" # 여기서 이미 return값이 결정 됨! => 그럼 나머지 case들은 아직 return값이 결정이 안 됐으니까 밑에에서 case를 따져서 결정 해줘야 돼! 
            # 그럼 나머진 아직 return값이 결정이 안 났어! 
            # 아래에서 내주면 돼!! 
            else:
                stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

answer = []
for i in range(N):
    bracket = input() # 괄호를 6번 입력을 받자...! 
    answer.append(solution(bracket))

    
print("\n".join(answer))



