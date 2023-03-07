from itertools import permutations # 순열 사용! => 1,3 != 3, 1
from itertools import combinations # 조합 사용! => 순서가 바껴도 상관없이 1개로 치부
from itertools import product # 중복 순열 : 중복까지 포함 
from itertools import combinations_with_replacement # 중복 조합 
import itertools

import sys

# 
arr = [-0,-7,-5,5,7]
arr2 = sorted(arr)
print(arr2)

result = list()


# 누적합 : itertools 
# sum = itertools.accumulate([1,2,3,4,5])
# print(list(sum)) # [1, 3, 6, 10, 15]

# arr = ["A", "B", "C"]
# result = list(permutations(arr, 2)) # len(arr)에서 2개 즉, 3p2
# print(result)


# # 조합 3c2 
# result = list(combinations(arr, 2))
# print(result)


# # 중복순열 : 중복을 포함해서 2개를 선택하도록,, => 역시 순서가 바뀌면 다른걸로! 
# result = list(product(arr, repeat=2)) # 2개를 고르겠다..! 
# print(result)
# # 중복조합 : 중복을 포함하는 조합! 

# result = list(combinations_with_replacement(arr, 2))
# print(f"중복조합 >> {result}")

# ## 입력받기 
# # 여러 줄을 input으로 하면 좀 그래...! 

# input = sys.stdin.readline

# data = input().rstrip() # '\n'까지 입력을 받기 때문에, \n은 제거하는 rstrip
# # 그럼 이제 정수도 입력 받을 수 있다...! 








# # 일단 조합을 활용해서 숫자 합을 만족시키는 값을 구해보자..! 
# nums = [-7,-5, -2, 2, 5,7] 
# # 0을 만족시키는 값을 조합을 구하자...! 
# result = list(combinations_with_replacement(nums, 2))
# print(f"result >> {result}")

from itertools import combinations # 조합 사용! => 순서가 바껴도 상관없이 1개로 치부

# print(f"answer >> {answer}")
## 풀어버림..! 

# 삼총사 => 바로 5분만에 풀어버림.. => 조합 문제인데, 거기서 조건 걸어주면 끝..! 

arr = [2,1,3,4,1]
result = list(combinations(arr, 2)) # 조합 순열은 중복이 안 돼! => 중복 포함이면 중복조합, 중복순열 쓰면 돼;..! 
sum_arr = []
for i in result:
    sum_arr.append(sum(i))

setArr = set(sum_arr)
print(sorted(setArr))
# print-(result)