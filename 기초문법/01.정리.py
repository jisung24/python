# 변수와 상수 

# 변수 : 값을 담을 수 있는 그릇 
# = (값을 넣는다! 값을 바꿔준다! 라고 생각하면 돼!)
a = 10
a = 19 # 재할당 해줄 수 있어
b = 15
b = 45 
print(b)

# 사칙연산 : 계산기 
a = 31
b = 5 
print(a + b)
print(a - b)
print(a * b)
print(a / b) # 그냥 일반 나누기 : 소수점도 나옴 
print(a // b)
print(a % b) 


# 👉 문자열 : 작은 or 큰 아무 따옴표나 사용해도 돼! 

# 문자열 덧셈 가능 
a = "Dwd"
b = "wdwdw"
print(a + b)
# 문자열이 이어 붙여진다. 
# 이스케이프 문자 
print("\"평범\"의 연속은 \"비범\"이다")

# 문자열 인덱싱 : 인덱스로 접근이 가능 
a = "dsadasdad"
print(a[3]) 

# 문자열 슬라이싱 
# 부분 문자열을 잘라올 수 있다 
print(a[:3]) # 처음부터 2번까지 만 가져온다
print(a[1:5]) # 1번에서 4번까지만 가져온다 
print(a[:]) # 전부 다 가져옴! 
print(a[::-1]) # 원본을 reverse시켜서 가져옴 

# 잘라서 더해줄 수 있어...! 
print(a[:4] + a[4:6]) # 더한다

# 범위를 벗어날 경우 원래는 인덱싱 할 때 에러가 나야 하지만,
# 슬라이싱을 할 땐 벗어나도 에러가 나지 않는다. 

# ❗️파이썬에서 값을 가져올 순 있지만 다른 것으로 값을 바꿀 순 없다❗️


# 👉 리스트
#  1. 리스트 인덱싱 슬라이싱 가능 
#  2. 리스트 덧셈이 가능(이어붙여짐)
#  3. 곱도 가능하다 (똑같은 리스트가 반복)
#  4. 중첩도 가능 
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(arr[0][2])
#  5. 리스트는 가변 객체여서 원하는 값으로 값을 바꿔줄 수 있다. 

# 리스트 초기화 방법 
arr = [5] * 8 # 같은 원소 8번 반복!

# 4 * 5의 크기를 갖는 2차원 리스트 초기화! 
arr = [[i] * 5 for i in range(4)]
# i에는 0에서 3까지 4개의 수가 들어가고 그걸 []로 감싼 후 5개를 만들어준다
print(arr)


## 객체 : 딕셔너리 
data = {} # 중괄호를 이용한 초기화 
data["apple"] = "사과"
print(data)
data["banana"] = "바나나"
data["melon"] = "멜론"
# key를 배열로 만들기...! 
# - list(객체.keys()) : 무조건 list로 형 변환 시켜줘야 돼! 
keys_arr = list(data.keys())
print(keys_arr[0])

# - list(객체.values()) : 값을 배열로 가져온다!
answer = ''
for i in keys_arr:
    # 키를 하나씩 가져온다..!
    answer += i + " "

print(f"key >> {answer}")


for i in keys_arr:
    print(f"{i} : {data[i]}") # 이런식으로 접근이 가능함! 


arr = [1,2,3,4,44,3,2,1,2,3,4,5,6,788,7]
# 각 원소가 몇 번 등장했는지...! 

# key가 있는 지 확인..! 
# for "key" in 객체 => 있는 지..! 
# for "key" not in 객체 => 없는 거..
dic = {}

for i in arr:
    if i not in dic: # i라는 속성이 dic에 없다면..! 
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)

# 특정한 data가 등장한 적 있는..지 확인! 3이 중복 등장했는지 확인한다! 
# stack에 넣어준다...! 
arr = [1,2,2,3,4,4,4,3,4,5,6]
stack = [arr[0]]

# 4가 stack에 len에 들어갈 때 까지 반복문 돌려줌..! 
i = 0
while True:
    if stack[len(stack) - 1] == 4:
        break
    else:
        stack.append(arr[i])
        i += 1

print(stack) 


# 3강 
# 코테에서 활용되는 파이썬 문법 

# 반복문 
# 만약 어떤 배열의 원소로 접근하고 싶을 때
arr = list(range(0, 11))
for i in arr: # arr의 각각 원소가 i가 되는거야...!! 
    print(i)


# map filter 사용하기 
arr2 = [i * 2 for i in arr] # arr에서 i를 왼쪽에 i * 2로 바꿔준다. 
print(arr2)

arr3 = [i - 1 for i in arr2]


# filter는 조건을 오른쪽에 써준다..! 
arr = [3,4,5,5,3,3,4,3,2,1,2,3,3,4]
# 3등급 맞은 학생의 수를 출력한다...? 
# 그럼 set으로 할 수 있지만...
three = [i for i in arr if i == 3]
print(f"3등급 맞은 학생의 수 >> {len(three)}")


# 숫자 범위로 접근하기...! 
# 1부터 50까지의 수 중에서 10의 배수만 더하는 프로그램! 
nums = list(range(1, 51))
ten = [i for i in nums if i % 10 == 0]
print(sum(ten))

# enumerate함수를 range대신 사용하면 index까지 가능 
arr = [3,4,5,6]
for i, ele in enumerate(arr):
    print(i, ele)


# 구구단 
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")


# 1부터 N까지 수 중 소수를 찾는 프로그램...! 
# n = 10
N = 10
for i in range(2, N + 1):
    print(f"{i} >> ")
    arr = []
    for j in range(1, i + 1):
        if i % j == 0:
            print(f"{j}")
            arr.append(i)

    if len(arr) == 2:
        print(f"{j}는 소수!")


# list중에서 가장 큰 값의 위치를 반환하는 함수를 구하자..! 
def findMaxValueList(arr):
    maxValue = max(arr)
    # 값을 찾는 배열 함수...가 뭐였더라..? 
    return arr.index(max(arr))
    # arr.index(원하는 값) : 즉 원하는 값의 index를 찾아주기 위한 값...! 

print(findMaxValueList([3,4,5,6,7,8,9,100,323,1,2,3,4,5,6,7,8,9])) # 8잘 나옴..! 


# ⭐️ 코테에서 자주 사용되는 라이브러리 ⭐️

# 👉 배열의 합 : sum(arr)
# 👉 배열에서 가장 큰 값 : max(arr)
# 👉 ... 가장 작은 값 : min(arr)
# 👉 ... 정렬 : sorted(arr)

# 정렬 
arr = [3,1,4,5,3,2,1,4,6,7]
sort = sorted(arr, reverse=True) # 내림차순 정렬 
# sorted(배열) : 배열을 정렬해서 새로운 배열을 반환한다 => 즉, 원본을 건들지 않는다. 

arr = [3,1,2,4,6,3,2,1]
newArr = sorted(arr, reverse=True)
print(newArr) # arr을 내림차순 정렬! 
inc_sort = sorted(arr, reverse=False) # 오름차순, reverse를 사용하지 않으면 자동 오름차순으로 정렬이 된다. 