# # 자연수 n은 100000 => 10^5 n이나 nlogn으로 풀어야 해..! 

# import sys
# # 소수의 개수 
# # 2부터 그 정수의 int(루트)만큼만 판단하면 돼..!  


# # 10보단 크고.. 20보다 같거나 작은 소수...! 
# def solution(number):
#     # 숫자...에 대한 소수! 
#     # 1. 분할해서 한 번 사용하기..! 
#     primeNum = 0
#     for i in range(number + 1, number * 2 + 1):
#         # 11부터 20까지....
#         count = []
#         # print(i, "가 소수인 지 검사 해볼게요....")
#         for j in range(2, int(i ** 0.5) + 1):
#             # 2부터 루트 11까지 검사.... 
#             if i % j == 0:
#                 # 나눠지는 게 있으면...! False이다. 
#                 count.append(j)
#         if len(count) == 0:
#             # 만약 담긴 게 없다면.....
#             primeNum += 1

#     return primeNum
# # 나는 일단 => 그냥 값을 구해주는 함수를 썼어....! 
# # 몇 개 인 지...

# answer = ''
# while True:
#     number = int(sys.stdin.readline()) # 숫자 입력을 받음..
#     if number == 0:
#         break
#     else:
#         answer += str(solution(number)) + '\n'

# print(answer)

# 시간 초과...! 


# 일단 소수가 맞는 지... 먼저 돌려주는 함수를 짜보자..! 

def isPrime(number):
    end = int(number ** 0.5)
    answer = True
    for i in range(2, end + 1):
        if number % i == 0:
            answer = False 

    return answer

# 소수인지 아닌 지 프로그램 짜 줌... 
while True:
    count = 0
    N = int(input()) # 숫자를 입력받아줌...! 
    if N == 0:
        break
    else:
        for i in range(N + 1, N * 2 + 1):
            if isPrime(i):
                count += 1
    print(count)
    
