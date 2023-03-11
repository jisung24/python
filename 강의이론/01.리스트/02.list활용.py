# 반복문이 array list(파이썬은 list)와 많이 사용된다. 
# array는 메모리 상에서 순차적으로 연속적으로 저장이 됨 
# 반복문이 순차적으로 반복이 되니까 배열이랑 자주 사용 됨! 

# ❗️배열의 두 숫자를 더해서 target이 될 수 있으면 true 아니면 false❗️

arr = [4,1,9,7,5,3,16]

# 1. 문제 이해하기 
# 👉 step1 : 직관적으로 생각하기 => 2중 돌면서 선택하기 

# for i in range(1, len(arr)):
#     print(arr[i-1], arr[i])

# # 그냥 연속하는 숫자면 저렇게 한 번에 연속하는 원소 넣을 수 있다! 
# # 근데 모든 경우의 수를 다 찾아야 하는 문제기 때문에 완전 탐색이 필요하다. 

# arr = [1,2,3,4,5,6,7,8] # 연속하는 3개를 한 번 돌아보자! 
# for i in range(2, len(arr)):
#     print(arr[i-2], arr[i-1], arr[i])


# 연속된 세 정수를 더해서 12가 되는 경우 3 4 5

num = 5
total = 5

arr = list(range(1, num + 1))
sumOfArr = sum(arr)
print(sumOfArr, total) # 같아질 때 까지..! 

while sumOfArr != total:
    # 같아지면 나온다! 
    if sumOfArr < total:
        # print("여기 들어옴!")
        arr = [i + 1 for i in arr]
        sumOfArr = sum(arr)
    
    if sumOfArr > total:
        # print("여기 들어옴!!")
        arr = [i - 1 for i in arr]
        sumOfArr = sum(arr)

    
print(arr)

# 자 결국 큰 수에서 total이 되든 작은 수에서 total이 되든 
# total이 되고자하는건 똑같은거잖아!! 

# while sumOfArr != total: ❗️ 이렇게 접근을 해야한다 ❗️