import sys

tc = int(sys.stdin.readline()) # \n까지 같이 받지만 int로 바꿔주기 떄문에 상관업서..! 
answer = ''
for i in range(tc):
    num1, num2 = map(int, sys.stdin.readline().split(' '))
    answer += f"Case #{ i + 1 }: {num1 + num2}" + '\n'

print(answer)