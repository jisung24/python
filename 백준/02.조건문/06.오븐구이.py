# 시간 0 - 23
# 분 0 - 59
hour, min = map(int, input('').split(' ')) # 한 라인씩 받는거구나...! 
# 일단 14 20 한 줄 받고
cookTime = int(input()) # 또 밑에라인 입력받고...!!! 

def finishTime(hour, min, cookTime):
    min += cookTime # 요리하는데 걸리는 시간을 더 해...! 
    if min >= 60:
        addedTime = min // 60 # 몫 나누기...! 
        min -= (60 * addedTime) # 120분이 더해지면 120을 빼줘야 돼!
        hour += addedTime
        if hour >= 24:
            hour -= 24
    print(hour, min)

finishTime(hour, min, cookTime)