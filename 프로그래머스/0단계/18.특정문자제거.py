# 파이썬 배열 문자열 왔다갔다..! 

arr = [1,2,3,4,5]

# ❗️파이썬에서의 split은 아무 파라미터를 넣어주지 않으면 빈칸을 기준으로 나눔❗️
str = "hello my name is jisung!"

# 구분자는 사라진다는 걸 알아야 돼 => 응용! 
str_arr = str.split() # 띄어쓰기를 구분자로 해서 배열로 만들어줌
print(str_arr)

newList = str.split(maxsplit=2) 
# 즉, 구분자를 2개만 구분해서 넣어주겠다는 의미 
# 띄어쓰기를 앞에서 부터 2개만 해주고, 나머지 띄어쓰기는 그대로 출력...! 
# 즉 배열의 길이는 그럼 maxsplit + 1이 되는거야
print(newList)
# ['hello', 'my', 'name is jisung!']


newList2 = 'a,b,c,d,e'
list2 = newList2.split(',', maxsplit=3) 
# , 3개까지 해주고 나머지 ,는 그냥 하나의 원소로 만들어줌 
# 배열의 길이는 4가 됨! 
print(list2) # ['a', 'b', 'c', 'd,e']



# splitlines() : 한 줄 단위로 나뉨.. 
i = '''
hedwdwdadawd
dwdawdawda
wdawdawdawd
wdwd
ddgggwe
fgbbbb
''' # split('\n')
print(i.splitlines()) 







str = "dwdwdwdaa"
arr = [i * 3 for i in str]
print(''.join(arr))

# 배열을 그냥 이어주기..! 

# 깃 