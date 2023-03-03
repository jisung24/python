def solution(angle):
    answer = 0
    if(0 < angle and angle < 90):
        answer = 1
    elif(angle == 90):
        answer = 2
    elif(90 < angle and angle < 180):
        answer = 3
    else:
        answer = 4

    return answer
# 어차피 angle은 1도에서 180까지만 이라고 나와있음 
# else 써줘도 돼! 

# 조건문에서 연산자를 적절하게 사용할 줄 아는지! 
# and or not , elif나.. 