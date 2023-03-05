# 배열에서 최댓값 2개를 찾자! 
# 정렬을 알아야 함 
# 배열과 문자열 오가는 문법 

# 전체 거꾸로 뒤집기 (배열 한에서만 reverse가 통함)
arr = [2,4,4,5,7,8,8,2,1,100]
arr.reverse() # 원본을 수정해줌 
# print(arr)


# sort vs sorted 
# sort : 기존의 배열을 바꾼다
# sorted : 기존의 배열을 변경❌ 새로운 list를 만든다. 

# 일단 실습은 sorted 즉, 원본을 변경하지 않는 sorted를 사용해야지 
arr = [4,5,56,6,7,8,9]
arr.sort(reverse=True) # reverse가 False이면 오름차순 True라면 내림차순 정렬!
print(arr) # sort는 원본을 바꾸니까...! 

arr2 = [1000,30,45,68,77,98,25]
arr2.sort(reverse=False) # 오름차순 => False는 애초에 default값이라서 안 써줘도 된다. 
# 즉, default값이 오름차순 
# True를 주면 내림차순. 


## sort key속성!  
# 각 요소에 적용되는 lambda함수를 적용할 수 있다.  
students = [
    {"name" : 'kim', "age" : 20 },
    {"name" : 'kim', "age" : 15 },
    {"name" : 'kim', "age" : 7 },
    {"name" : 'kim', "age" : 27 },
]

# 학생 나이순으로 정렬! 
students.sort(key = lambda student : student.age)
print(students)