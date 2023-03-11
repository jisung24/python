import sys
N = int(sys.stdin.readline().rstrip('\n')) # 정수 하나를 입력받음 
#

numbers = int(sys.stdin.readline().rstrip('\n'))

#  ㅇㅋ 입력 받아줌...! 
def solution(numbers):
    # 정수의 합을 return 
    arr = list(map(int, list(str(numbers))))
    return sum(arr)

print(solution(numbers))