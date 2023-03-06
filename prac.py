a = 10



## replace로 값 제거해준다!! 

my_string = "nice to meet you"
arr = ["a","e","i","o","u"]


for i in my_string:
    for j in arr:
        if i == j:
            new_arr = my_string.replace(j, '')

print(new_arr)





a = "How are you? Python3"
a= a.upper()
print(a)


a = a.replace("O", "")
print(a)

## 문자열 배열로 바꾸기...! 
n = 1234
print(list(map(int ,list(str(n)))))
# 하나씩 바꿀거면..그냥 list로 해줘,..! 

## 문자열, 숫자를 배열로 바꾸기...! 
str1 = "dwdadadada"
print(list(str1)) # 그냥 하나하나로 각각 쪼개기..! 
print(" ".join(list(str1))) # 띄어쓰기 기준으로 각 배열의 원소를 문자열로 바꿔주겠다..! 


str2 = 12345
lists = list(map(int, list(str(str2))))
print(lists)

# 숫자를 문자열로 바꿔주기! 
value = ''.join(map(str, lists))
print(value)

# 숫자형 배열을 문자열로 바꿔줄 떄는 각 모든 숫자들을 map을 통해서 str로 바꿔준다음 join을 진행해야한다. 



nums = 1223313131
# 배열로 바꾸기
value = list(map(int,list(str(nums))))
print(value)

rejoin = ''.join(map(str, value))
print(rejoin)