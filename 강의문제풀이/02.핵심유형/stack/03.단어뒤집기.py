
# < 가 나왔을 떈 stack에 넣어줌 
# 그럼 >가 나오면 stack에서 빼주고..! 
# 그리고 단어들이 stack이 비어있을 때 나온 단어는 <안에 적히지 않았다는 것! 
# 따라서 뒤집어준다...! 

# 문자열 종류 
# 소문자, 숫자, 특수문자, 공백 => 공백 조심하자...! 
# 양 끝이 공백으로 시작하는 경우는 없음 trim안 적어줘도 돼! 

# 공백까지 stack에 넣고 출력해주면 돼!!! 

# 특수 문자만 들어가는 stack




# 괄호 밖에 있더라도 그 문자들을 한 번에 다 모아서 뒤집어주면 안 돼!
# 단어 기준으로 뒤집어줘야 해서, 공백을 만나면 모아뒀다가 pop! 
# <안에 있는 건 그냥 += 해주면 되고....! 
S = input() + " "

stack = []
answer = ''
for i in range(len(S)):
    if S[i] == "<":
        stack.append("<")
        answer += "<"
    elif S[i] == ">":
        stack.pop()
        answer += ">"
    else:
                # print(i)
        if stack:
            answer += S[i]
        else:
            if S[i] != " " or S[i + 1] != "<":
                stack.append(S[i])
            else:
                # 스택이 비어있을 떄 까지...계속...
                while True:
                    if len(stack) == 0:
                        answer += ' '
                        break
                    else:
                        answer += stack.pop()

print(answer)


# 틀림...! 