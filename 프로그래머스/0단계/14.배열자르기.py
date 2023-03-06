def solution(numbers, num1, num2):
    # index num1에서 num2까지 자른 배열을 return 하자! 
    return numbers[num1:num2 + 1]

# list 슬라이싱
list = [1,2,3,4,5,6,7,8,9,10]
# 2배씩 하고,,, 잘라보자! 
multy = [i * 2 for i in list] # list라는 배열을 가져와서 2배씩 해준다.
print(multy[1:3]) # index 1부터 2번까지 
print(multy[3:]) # index 3부터 끝까지! 

# 문자열, 배열 뒤집기에 모두 잘 쓰임 => slice 
print(multy[::-1]) # index 뒤집어서 전체를 return 