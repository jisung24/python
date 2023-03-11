# 1. 입력받을 때 공백처리 
# 2. n은 100 => 10의 4제곱 미만으로 풀어야 해! (반복문 최대 3번까지 쓸 수 있어)

def checkBrackets(bracket):
    # 문자열을 입력받고, True인지 확인..! 
    # 무조건 소괄호와 대괄호로 이루어져 있음..! 
    # open = ["(", "["]
    # close = [")", "]"]
    stack = []
    # 문자열은 무시해줘도 됨..! 
    for i in bracket:
        if i == "(" or i == "[":
            # 만약 여는 괄호 아니면 닫는 괄호가 나오면
            stack.append(i) # 값을 넣어준다 
        elif i == ")": # "("
            # error! 
            if not stack or stack[-1] != "(": # [ 이 괄호가 들어잇을 수 있어.
                return "no"
            else:
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] != "[":
                return "no"
            else:
                stack.pop()
        else:
            # 나머지는 그냥 무시..! 
            # 문자열은 갈 길이 사라져서 다음으로 안 넘어가. 
            # ❗️ 모든 조건을 잘 따져줘야 한다 ❗️
            continue

    # 반복문 빠져 나와서..! 
    if not stack:
        return "yes"
    else:
        return "no"

answer = ''

while True:
    # 처음도 역시 공백이 올 수 있어! 
    #  . => 
    # 근데 처음 공백은 제거하면 안 되는게
    #  .도 입력을 계속 받게 해줘야 돼
    bracket = input() # 인자를 전달하지 않으면 그냥 공백을 제거한다.
    # 공백은 고려 안 해줘도 된다
    # 무조건  .로 끝난다고 문제에 쓰여져 있고, 처음 공백은 입력을 받아줘야 하는 의무가 있다 


    if bracket == '.':
        break
    else: # 마침표가 아닌 다른 게 오면
        answer += checkBrackets(bracket) + '\n'

print(answer)