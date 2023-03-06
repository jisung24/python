strlist = ["We", "are", "the", "world!"]
# 각 원소의 길이로 바꿔줘..! 

# 1. map을 사용해서 x : len(x)사용하거나... 
# 2. list 컴프리헨션 ...! 

len_arr = [len(i) for i in strlist]
print(len_arr)


# filter를 사용하려면 조건식을 써야하는데 조건식은 맨 오른쪽에 사용하면 돼! 
lists = [1,2,3,4,5,6,7,8,9]
lists2 = [i for i in lists if i % 2 == 0] # 2 4 6 8 
print(lists2)