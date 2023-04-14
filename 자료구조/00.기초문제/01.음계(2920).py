# 입력 받기

# 1부터 8까지 나온다면 ascending 
# 계속 낮아진다면 
# 그게 아니라면 


# 쭉 탐색을 해서 이거인지 아닌 지 결과를 내는 방법 
# 처음에 A라고 설정을 하고 변화를 설정해준다. 
asc = True 
des = True 

data = list(map(int, input().split(' '))) # list로 담아준다! 

for i in range(1, 8):
    # index 0번부터! 
    if(data[i - 1] < data[i]):
        des = False
    elif(data[i - 1] > data[i]):
        asc = False

if(asc):
    # 오름차순이 참일 경우! 
    print("ascending")
elif(des): # 내림차순이 참일경우
    print("descending")
else: # 둘 다 아닐 경우 => Mixed! 
    print("mixed")