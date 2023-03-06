# 어떤 자연수 n이 있으면 n초과 2n이하의 범위에는 적어도 1개의 소수가 존재한다. 

def isPrime(number):
    if number == 1:
        return False
    # NUMBER가 1이 아니라면 자연스업게 밑으로 옴..! 
    for i in range(2, int(number ** 0.5) + 1): # 그 수를 2부터 그 수의 저 범위까지만 계산해주면 알 수 있다..! 
        if number % i == 0:
            return False
    
    return True 

def primeCnt(nums):
    count = 0
    # 입력받은 수를 여기다가 대입하면.... n초과 2n까지 반복문을 돌려서 개수를 세 줌..! 
    for i in range(nums + 1, (nums * 2) + 1):
        if isPrime(i):
            # 소수가 맞다면...
            count += 1

    return count

answer = ''
while True:
    count = 0
    nums = int(input())
    if nums == 0:
        break
    else:
        # 범위가 도대체 몇 개가 나오는 지...! 
        answer += str(primeCnt(nums)) + '\n'

print(answer) 


# 나는 모든 수에 대해서 소수인지 아닌 지를 검사해줘서 시간 초과가 계속 뜨는 것 같다. 
# 그래서 미리 입력받은 수에 대해서 소수인지를 판별해주는 작업이 필요하다..... 