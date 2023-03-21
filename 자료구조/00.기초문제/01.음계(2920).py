# 오름차순인 지 아닌 지! 
# 1. 오름차순인지 만 확인한다. 
# -1) 오름차순일 경우 count가 풀로찬다. 
# -2) 내림차순 일 경우, count == 0
# -3) mixed일 경우 풀 0 둘 다 아닌 다른 자연수

arr = list(map(int, input().split()))
count = 0
for i in range(1, len(arr)): # 0부터 arr의 길이 -1 까지.. 
    if(arr[i - 1] <= arr[i]):
        count += 1
    
if count == len(arr) - 1:
    print("ascending")
elif count != 0:
    print("mixed")
else:
    print("descending")


# 나동빈 풀이 
# 오름차순 True 
# 내림차순 True 
# 둘 다 False로 바뀌면 mixed ...! 

# inc = True
# dec = True
# for i in range(1, len(arr)):
#     if(arr[i - 1] < arr[i]):
#         dec = False
#     elif(arr[i - 1] > arr[i]):
#         inc = False

# if(dec == True):
#     print("descending")
# elif(inc == True):
#     print("incending")
# else:
#     print("mixed")