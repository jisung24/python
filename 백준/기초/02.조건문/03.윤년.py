# 윤년이면 1 아니면 0


year = int(input()) # 년도 입력받음 

def isYoonYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0

print(isYoonYear(year))