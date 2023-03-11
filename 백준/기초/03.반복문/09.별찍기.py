# 1 => 1개  2는 2개  n은 n개! 

number = int(input())
answer = ''
for i in range(1, number + 1):
    # 1,2,3,4,5
    for j in range(1, i+1):
        answer += ("*")
    
    answer += '\n'

print(answer) 