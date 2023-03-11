# 45분 일찍 알람 설정하자..!  

# 시간을 입력받고 45분을 빼주자..! 
time, minutes = map(int, input().split(' '))
# 배열을 전부 int형으로 바꿔준다..! 

def checkAlertTime(time, minutes):
    minutes -= 45 # 일단 45분을 빼준다..! 
    if minutes < 0:
        minutes += 60
        time -= 1
        if time < 0:
            time += 24

    print(time, minutes)
checkAlertTime(time, minutes)