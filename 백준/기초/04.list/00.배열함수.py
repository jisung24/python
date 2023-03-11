# 반복문 한 번 돌려보자! 
arr = [1,2,3,4,5]
for i in range(0, len(arr), 2):
    # 즉 시작부분을 생략하면 0부터
    # len(arr)이니까 len(arr) - 1까지!
    # i가 2씩 늘어난다! 
    print(i)



for i in range(1, 21, 3): # 1 4 7 10 ~~ 19
    print(f"i >> {i}")



# 1. 값 추가 
# - append : 맨 뒤에 값을 추가
# - insert(a, "추가할 값") : 지정한 a번 index에 값 추가 

arr = [1,2,3,4]
arr.append(5)
arr.insert(2, 1000) # index 2번에 1000 append한다.
# INSERT : 즉, 중간에 삽입하려면 뒤에 있는 값들이 계속 뒤로 밀려난다..! 
# javascript splice와 비슷함. 

print(f"arr >> {arr}") # list 잘 뜨네? 



# 2. 값 삭제 
# - pop(index) : 원하는 위치에 있는 값을 return한다.! 
# index가 마이너스 일 경우, 뒤에서 몇 번째 값 제거.. 라고 생각하면 돼! 
# [1,2,3,4,5]
# pop(-2)면 뒤에서 2번째 값 4가 return이 돼! 
my_list = [1,2,3,4,5,6]
value = my_list.pop(3)
print(f"삭제한 이후의 배열 >> {my_list}")
print(f"삭제한 값 >> {value}")

value2 = my_list.pop(-1)
print(value2) # 뒤에서 첫 번째 값(원본 배열에서 이미 삭제 됨)
print(my_list) # 1 2 3 5
value3 = my_list.pop(-2) # 3(-가 붙으면 뒤에서 몇 번째 값으로 해석이 돼! )
print(value3) # 1 2 3 4


# - list.remove("삭제할 값 ") : return값이 없어! => pop은 그냥 javascript처럼 삭제한 값이 반환이 됨. 
# 하지만 remove는 반환되는 값이 없어...! 


# del : 마찬가지로 원본을 바꾼다. 
# pop은 지정한 index 1개만 삭제 
# del은 범위를 지정해서 한 번에 삭제할 수 있음.
lists = [1,2,3,4,5,6,7,8,9,10]
del lists[0] # index 0번 삭제
print(lists)
del lists[-2] # 뒤에서 2번째 까지 삭제
print(lists)
del lists[2:4] # index 2번부터 3번까지만 삭제한다. 
print(lists)
del lists[:] # 전부 삭제한다. 
print(lists)
