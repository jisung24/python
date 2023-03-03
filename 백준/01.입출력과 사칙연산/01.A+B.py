num1, num2 = input("").split(' ') # 입력받은 수를 문자열로 받아서 split으로 쪼개줘야 함.! 

def add(num1, num2):
    return int(num1) + int(num2)

print(add(num1, num2))