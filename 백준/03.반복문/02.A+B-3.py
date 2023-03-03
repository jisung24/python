tc = int(input('')) # tc = 5
answer = ''

def plus(num1, num2):
    return num1 + num2

for i in range(1, tc + 1):
    # 1부터 5까지 받아야 하니까 tc + 1을 해야 -1해서 tc가 된다.
    num1, num2 = map(int, input().split(' ')) # 입력을 받아주고... 
    answer += (str(plus(num1, num2)) + '\n')

print(answer)
    
