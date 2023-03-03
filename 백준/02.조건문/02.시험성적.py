# python은 조건문이 별로 없음. 

# 딕셔너리(javascript객체) 이용하거나 elif
testScore = int(input(''))

def checkClass(testScore):
    if 90 <= testScore and testScore <= 100:
        print("A")
    elif 80 <= testScore and testScore <= 89:
        print("B")
    elif 70 <= testScore and testScore <= 79:
        print("C")
    elif 60 <= testScore and testScore <= 69:
        print("D")
    else:
        print("F")

checkClass(testScore)






# 파이썬 and or not연산자 
# and 
# or
# not