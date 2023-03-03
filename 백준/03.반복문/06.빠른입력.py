import sys
# input으로 입력받으면 느림.

# input ====> sys.stdin.readline
# 반복문으로 여러 줄을 입력 받아야 할 떄! 

tc = int(sys.stdin.readline()) # 이건 1개니까 input으로 입력받아줌. 
answer = ''
# 5번이니까 
def fastSum(tc):

    for i in range(tc): # 0 1 2 3 4 아무튼 5번! 
        num1, num2 = map(int, sys.stdin.readline().split(' '))
        answer += str(num1 + num2) + '\n'
    return answer

print(fastSum(tc))

# 그럼 정수 1개도 그냥 sys.stdin.readline받으면 되는 거 아니야? 
# => 한 줄 단위라서 \n을 입력을 같이 받아버림 3\n로 입력이 받아짐
