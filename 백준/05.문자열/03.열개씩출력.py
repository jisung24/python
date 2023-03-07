str1 = input() # 문자열이니까... 바로 입력을 받음...! 
answer = ""

for index, value in enumerate(str1):
    if index % 10 == 9:
        answer += value + '\n'
    else:
        answer += value

print(answer)

# enumerate 
arr = [1,2,3]
arr2 = list(enumerate(arr))
print(arr2[0][1]) # [(0,1), (1,2), (2, 3)] 
# 2차원 배열이라고 생각하고 접근이 가능하다...! 