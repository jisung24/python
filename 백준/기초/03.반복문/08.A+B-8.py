import sys

tc = int(sys.stdin.readline()) 
answer = ''
for i in range(tc):
    num1, num2 = map(int, sys.stdin.readline().split(' '))
    answer += f"Case #{i+1}: {num1} + {num2} = {num1 + num2}" + '\n'

print(answer)