import math # math함수 사용함 
import sys # sys로 입력을 받음 

# 리스트 문법 


# 1) 리스트 생성
# - 대괄호 
arr = [1,2,3,4,5,6] # 자바스크립트와 생성 방법 같음  
# - 반복문 이용해서 배열 한 번에 초기화 
# 1부터 20까지 배열 생성
arr2 = list(range(1, 21))
print(arr2)
arr3 = list(range(1, 31, 3)) # 1부터 30까지 3씩 계속 늘어나는 수 생성 1 4 7 10 13...  
# list() : Array.from()이라고 봐도 돼! => 배열로 만들어주는 문법이야


# -2) 리스트 연산 (더하기 곱하기 섞어서 사용할 수 있음)
# - 더하기 (리스트 이어붙임)
arr4 = [1,2,3,4,5]
arr5 = [6,7,8,9]
arr6 = arr4 + arr5
print(arr6)

# - 곱하기 (리스트를 반복함)
arr7 = [1,2,3]
print(arr7 * 3 + arr6)

# 리스트 인덱싱 + 슬라이싱 

# - 인덱싱 : 접근, 검색, 값 수정(문자열과 다르게 수정이 가능함) 
# (신기하게도 파이썬에서는 음수로도 접근이 가능하다)
# 음수 : ex) -2면 뒤에서 2번째..! -4면 뒤에서 4번째 => 음수는 인덱스 개념이 아니야! 
arr8 = ["apple", "banana", "melon", "orange"]
print(arr8[-3]) # 뒤에서 3번째 : banana
print(arr8[2]) # melon

# - 슬라이싱 : 리스트를 필요한 부분만 잘라서 사용한다. 
# *** << 원본은 영향을 받지 않는다 >> ***
slicing = ["a","b","c","d","e","f","g"]
print(slicing[1:3]) # index 1 2번만 잘라서 사용! 
print(slicing) # 원본은 영향을 받지 않아! 

# 뒷부분 생략 : 끝까지
arr9 = slicing[1:] # 1부터 끝까지! 
print(arr9)

# 앞부분 생략 : 처음부터

# 즉, 둘 다 생략 [:]하면 처음부터 끝까지!!! 
arr10 = slicing[:4]
print(arr10)

######### 배열 함수 #########

# -1) len(배열이름) : 배열의 길이를 return해준다 

# -2) max(배열이름), min(배열이름) : 배열의 최댓값, 최솟값을 구해준다. 

# -3) sum(배열이름) : 배열 모든 원소의 합을 구해준다. 

# ======= << 삭제 >> =======
# list.pop(), del(list[]), list.remove(), clear()
# pop만 return값이 있다! => 범위로 삭제하고 싶을 떈 delete를 쓰고,
# 삭제한 값이 필요할 땐 무조건 pop을 써야함.

# -4) del(배열이름[범위 or 인덱스]) : 지정된 부분을 삭제한다.
# 단 del은 return값은 없고, 그냥 삭제만 해줌.  
arr11 = ["hello", "heello2", "hello3", "hello4"]
del(arr11[1:3]) # 1번부터 2번까지 2 3을 삭제한다.
print(arr11)

# -5) list.remove("삭제하고 싶은 값") : 배열에서 특정 값 제거한다. 
# 근데 만약 제거하고 싶은 값이 없으면 remove
# 이거 시간복잡도 많이 먹어서...! 
# 특정한 값을 제거 할 때는 그냥 ... 반복문 1번 돌려서 제거하는 게 맞대..! 



## map, reduce, filter
# 패턴 다 똑같아!!!!

# 파이썬에서 map사용하기 

def plus(x):
    return x + 1

arr00 = [4,6,8,9]
map_arr = list(map(plus, arr00)) # map()은 list type이 아니어서 list type으로 바꿔줘야 돼! 
# map(모든 원소에게 적용시켜줄 함수, map의 대상배열!)
print(map_arr)


# 파이썬에서 filter사용하기! 
arr = [2,2,2,4,5,89,21,19,41,44,14,14,41,14,99,141,41,44]
arr2 = [45, 53] # arr2[len(arr2) - 1]보다 큰 수만 filter
# 20이상의 수들만 걸러주기! 
def overTwenty(x):
    return x >= arr2[len(arr2) - 1]

filter_arr = list(filter(overTwenty, arr))
print(filter_arr)




arrr = [1,2,2,2,2,3,34,3,32,3,3,2,2,1,2,3,34,5]
set_arr = list(set(arrr)) # 각 종류! 
# 저 set에서 각각의 값이 arrr에서 몇 개가 있는 지..! 

print(arrr.count(3)) # 3의 개수 => 5개 
hash = {}
for i in range(len(set_arr)):
    hash[set_arr[i]] = arrr.count(set_arr[i])

print(hash)