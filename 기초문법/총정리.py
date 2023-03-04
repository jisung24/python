# 리스트 
# 순차적인 데이터를 나타내는데 사용된다. 

empty_list = [] # 빈 리스트 
nums_list = [1,2,3,4,5] # 숫자 리스트
mix_list = [1, "dwdw", 3] # 혼합 리스트 
two_list = [ # 이차원 리스트 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# list() 를 사용하여 문자열을 List로 바꿔줄 수 있다.!! 
print(list("hello world"))
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(list(range(4))) # 0 - 3까지 숫자를 생성한다. 

# ❗️ range 함수 사용법 ❗️
# - range(1, 11)은 1부터 10까지의 수를 생성한다. 
# - 👉 즉, 수를 생성하는 역할! 
print(range(1, 11))
print(range(11)) # 0부터 10까지
print(range(1, 11, 2)) # 1 3 5 7 9 2씩 증가시키는 함수.

# for i in range(1, 11):
# 1. range가 1부터 10까지의 수를 만드는데, 
# 2. 그 안에 있는 i라는거야..! 
# 3. 즉, i가 순차적으로 1 2 3 4 5 6 7 8 9 10이 온다는 말임. 

# 🔴 range() 함수의 결과는 반복가능(iterable)하기 때문에 for문을 사용해 출력할 수 있다. 🔴
for i in list(range(0, 8, 1)):
    print(i)


for i in range(10,0,-1): # 10에서 1까지 
    print(i)

for i in range(20, 0, -2):
    print(i)

# 쉽게 독해하는 법 : 숫자를 먼저 읽고 어떤 수 들 인지 한 번에 머릿속에 그린다. 
# 그리고 i가 하나씩 차지한다. 
# 왜냐면 range는 그냥 숫자를 1 3 4 5 짠 하고 띄워주는 함수야. 
# 그걸 list로 받으면 [1, 3, 4, 5]가 되는거구...!! 

li = [1,3,4,5]
answer = []
for i in range(0, len(li)):
    if li[i] > 3:
        answer.append( li[i] )

print(" ".join(str(s) for s in answer))


## ⭐️ 리스트의 연산 ⭐️
# -1) 리스트 더하기 (리스트1 + 리스트2) => 2가 1뒤로 옴 
# -2) 리스트 곱하기 (리스트를 원하는 횟수만큼 반복해준다)
arr = [2,4,6]
arr2 = [4,5,6]
arr3 = arr + arr2
print(arr3)
print(arr * 10)


## ⭐️ 리스트 인덱싱 + 슬라이싱 ⭐️
# 👉 인덱싱 : 그냥 접근하는 거! (❗️문자열과 다르게 수정이 가능하다❗️)
# 🔴 뒤에서 접근이 가능하다 🔴
arr4 = [2,3,4,5,6,7]
print(arr4[0])
print(arr4[-5]) # 뒤에서 5번째 값! 3
print(arr4[-4]) # 4

# 👉 슬라이싱 : 부분적으로 잘라서 추출해내는 것
print(arr4[0:3]) # idx 0번부터 2번까지
print(arr4[-4:-2]) # 뒤에서 4번째 값 부터 뒤에서 3번쨰 값 까지..! 
# [4 5]
sliced = arr4[-3:] # 뒤에서 3번째 부터 끝까지! [5,6,7]
print(sliced)
# ❗️슬라이싱은 index를 벗어나더라도 유연하게 대처해준다❗️
print(arr4[-4:10000]) # 4 5 6 7 => 에러를 내지 않는다. 
print(arr4[:]) # all elements
print(arr4[1:5:2]) # 2칸씩 뛰면서 1 3을 추출

## ⭐️ 리스트의 수정 ⭐️
# 👉 문자열과는 달리 배열의 내부값은 변경될 수 있다
arr5 = [1,2,3,4,5]
arr5[3] = [1000] 
print(arr5)

arr5[3:4] = [4,5,6] # 그냥 값처럼 smooth하기 들어간다.
print(arr5)


## ⭐️ 리스트 요소 삭제 ⭐️
lists = [2,4,6,7,8]
del lists[2:4] # 2 3번 요소 삭제
print(lists) # [2, 4, 8]



# 파이썬 map 
# 맵객체를 반환하기 떄문에 반드시 리스트로 형 변환을 해줘야 한다.
arr = [1,2,3,4,5,6]
def incOne(x):
    return x + 1

lists = list(map(incOne, arr))  # [2, 3, 4, 5, 6, 7]
print(lists)