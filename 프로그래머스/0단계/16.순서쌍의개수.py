# 두 개의 순서를 정하여 짝지어낸 쌍 
# 그럼.. 그냥 약수의 개수 구하면 되는 거 아닌가...? 
# 4 * 4도 허용..! 

# 1 2 4 5 10 20 25 50 100
def solution(n):
    arr = []
    for i in range(1, n + 1):
        if(n % i == 0):
            arr.append(i)

    return len(arr)




# 문법 
# 파이썬 버젼 구조분해할당 => 무조건 개수가 맞아야 한다. 
x,y,z = [1,2,3]   
print(x,y,z)

