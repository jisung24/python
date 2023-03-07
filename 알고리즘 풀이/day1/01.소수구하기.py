# n이 100만이야... 10^6 
# 웬만하면 n으로 풀어야 해...
# nlogn이나.... 

def isPrime(num) :
    # 그 수 부터... 
    answer = True
    end = int(num ** 0.5)
    for i in range(2, end + 1):
        if num % i == 0:
            return False
        
    return answer 



M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        # 함수가 true라면...
        print(i)
