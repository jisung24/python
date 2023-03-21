cards, num = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 1. 완전 탐색으로 풀기 
result = 0
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            sum_value = arr[i] + arr[j] + arr[k]
            if sum_value <= num:
                result = max(result, sum_value)
                # 둘 중 큰 값이 들어간다...! 

print(result)


# 21보다 작거나 같은 수 전부 filter해서 정렬 후 가장 
