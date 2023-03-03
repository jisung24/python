def solution(number):
    # number가 홀수인지 짝수인지는 모르겠는데.. number이하의 짝수의 합! 
    # number = 11 
    sum = 0
    for i in range(2, number + 1, 2):
        sum += i
    
    return sum