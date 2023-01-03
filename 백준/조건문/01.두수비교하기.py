num1, num2 = input().split(' ')

if (int(num1) > int(num2)):
    print(">")
elif (num1 == num2):
    print("==")
else:
    print("<")
