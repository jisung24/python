# 수 10개를 입력받고 이를 42로 나눈 나머지를 구한다..! 
# 그리고! => 서로 다른 값이 몇 개 있는 지 출력한다. 

# 서로 다른 값 => 값의 종류가 몇 개 있는 지 구하자..! 
# 해쉬 써도 되고, 그냥 중복따위 없애주는 set쓰면 끝! 

# 그냥 10번을 입력만 받으면 되는거야..! 
nums_arr = []
for _ in range(10):
    value = int(input())
    nums_arr.append(value % 42)

s = set(nums_arr)

print(len(s))