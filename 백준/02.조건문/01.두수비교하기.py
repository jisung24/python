num1, num2 = input().split(' ')

def compareNums(num1, num2):
    intNum1 = int(num1)
    intNum2 = int(num2)

    if(intNum1 > intNum2):
        print(">")
    elif(intNum1 == intNum2):
        print("==")
    else:
        print("<")

compareNums(num1, num2)


# 2가지 
# ❗️input함수는 무조건 문자열을 입력받는다❗️
# 형변환 문법 
# - int()  float()  str()  chr()  bool()
# - 정수      실수     문자열   문자    불린

print(float(3)) # 3.0 
print(int(3.44444)) # 3 (그냥 소수점이 사라짐)
print(chr(3) + chr(100)) # d찍임