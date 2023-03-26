# 삽입 정렬 
# 버블 정렬 선택정렬 삽입정렬 이렇게 3개는 아주아주 기본적인 알고리즘 

# 2번째 값 부터 끝 까지 하나씩 step마다 선택해서 
# 그 선택한 값을 정렬한다. 

arr = [8,5,6,2,4]
print(f"시작 >> {arr}")
for i in range(1, len(arr)):
    for j in reversed(range(0, i)):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

        else: break

print(arr)


# 실패! 