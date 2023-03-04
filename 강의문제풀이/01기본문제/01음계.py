# 8개의 음을 나타내는거라서 주어진 모든 숫자는 같은 게 없어! 
# 따라서 정렬 할 때, 숫자가 같다는 건 고려하지 않아도 돼! 

# 1 2 3 4 5 6 7 8이런식으로 입력받아야 해! 
lists = list(map(int, input('').split()))

# 여기서 이제 오름차순인지, 내림차순인지, mixed인 지
# 일단 2개만 고려해주고, 둘 다 False일 떄 mixed를 출력해주면 돼!  
ascending = True 
decending = True 

# 계속 반복문을 돌려서 앞과 뒤를 비교해가며.. 뒤에 것이 더 커야 돼! 
for i in range(1, len(lists)):
    if lists[i] > lists[i-1]:
        decending = False
    else:
        ascending = False

# 마지막에... True가 유지된 친구만...
if ascending:
    print("ascending")
elif decending:
    print("decending")
else:
    print("mixed")


# 코드 작성 tip 
# 1. 만약 boolean값이 있는 변수라면.. 그냥 변수만 조건문에 적어주면 된다. 
# 2. 만약 반복문을 돌리면서 값이 변할 지 아닌 지 지켜봐야 되는 상황이면 ,
# - 처음 값을 True로 하고 아닐 시 즉시, False로 바꿔주면 된다! 