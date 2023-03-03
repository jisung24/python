N = int(input())
arr = list(map(int, input().split(' ')))

# 일단 최댓값을 고르자! 
max = max(arr)



# 한 번에 바꿔주는 함수 없나...! 
for i in range(len(arr)):
    arr[i] = (arr[i] / max) * 100

print(arr)
print(sum(arr) / N)