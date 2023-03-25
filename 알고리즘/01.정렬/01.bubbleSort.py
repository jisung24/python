# 버블 정렬 횟수 
# length - 1번 반복한다! 

arr = [5,2,3,1]
count = 0
# cycle은 len(arr) - 1
for i in range(0, len(arr) - 1): # cycle 
    count += 1
    for j in range(1, len(arr) - i):
        if arr[j] < arr[j - 1]:
            swap = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = swap 
            print(arr)
    print(f"{count}번째 cycle!")
    print(arr)
print(arr)

# 버블 정렬은 한 번 순회를 돌아도 전부 배열이 되지는 않는다. 
# 단 가장 큰 수가 제일 뒤에 배치가 된다 