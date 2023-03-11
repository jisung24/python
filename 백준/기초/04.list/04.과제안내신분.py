# 1에서 30중에 하나씩 나오는 수를 제거하는 방법! 

# 1에서 30까지 수를 생성한 후에
# 반복문을 돌려서 나오는 수를 저 1에서 30 중 에서 제거한다. 
# 결국 제거하고 마지막으로 남는 수 


nums = list(range(1, 31))

# 원하는 값을 삭제할 수 있는 기능이 있어..! ==> remove함수!!! 
for _ in range(28):
    # 28번 해주면 돼 그냥! 
    value = int(input())
    nums.remove(value)

print(min(nums))
print(max(nums))