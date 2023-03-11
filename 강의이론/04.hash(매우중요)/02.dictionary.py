# 객체는 코테에서 매우 자주 쓰인다 
# 잘 활용해야 함
# 언제 써야하고, 어떤 연산을 써야하는 지! 

# 자 우리는 key를 지정하는데, 
# key가 어떤 게 오든 hash함수가 숫자로 잘 바꿔주니까
# ❗️그냥 이해를 할 때 key를 그냥 배열 index라고 생각하면 훨씬 편해..! 

stu = {
    'name' : '지성', # name => 1번 index에 지성 저장
    'age' : 26 # age => 2번 index에 26저장 
}

print(stu)

# 어떨 때 써? 
# 배열의 모든 요소가 각각 특징이 있어서 구별을 해줘야 할 때! 
# ex) 모든 홀수, 짝수의 개수 
# ex) 모든 원소가 각각 몇 번 나왔는 지!  => 1은 0번 2는 1번 


# ❗️ 매우 매우 매우 중요 ❗️
# key 접근 (key = index라고 했으니까 접근하는데 O(1) => 배열에서 index 접근하는데 O(1))
# 존재하지않은 key에 접근하면 안 된다! key error! 
# 근데 키가 1000개면 내가 어캐알아..? 
# 키 in 객체 => 있는 지 없는 지 검사해주는 문법 
print("height" in stu) # "height"라는 key가 stu에 있어? 라는 문법 

# 있는 지 없는 지 해시함수에 의해서 바로 알 수 있다..! 
# 배열에서 값 찾으려면 O(N)이 드는데, hash는 함수 때문에 바로 알 수 있음 
# O(1)
# 검색도 O(1)이 소요된다...! 
# 그래서 key로 보통 검색을 할 때!!!!!!!!!!! => O(1)이 소요됨
if "height" in stu:
    print(stu['height'])
else:
    stu["height"] = 100
    print(stu)



# 해시 : key가 index라고 생각하고, 
# 접근도 O(1)
# 근데 검색이 in연산자로 하는데, O(1)이야... 엄청난 혁신임.



# two sum문제 
# 접근 방법 
# 1. 직관적으로 생각하기 (대표적으로 완전탐색)
# 2. 자료구조 알고리즘 활용 (큐, 스택, 해시 등등..)
# 3. 시간복잡도를 줄이기 위해 메모리 사용 (❗️대표적으로 hash table❗️)


# 1. 숫자 1개에 접근해... 그래서 target에서 뺀 값이 key에 있는 지 검사! 
# 기억하고 싶은 게 있다면 key에 집어넣어야 한다..! 
# 
nums = [4,1,9,7,5,3,16]
target = 14
hashtable = {}

# hash초기화 O(N) : 이건 어쩔 수 없어! 
for i in nums:
    hashtable[i] = True # 뭔 값을 넣어도 상관없어! 
answer = []
for i in nums:
    # 값을 하나 찾아서.. 이 값이 있다면 10을 찾는다
    if i in hashtable:
        print(i,"부터 찾을게")
        if target - i in hashtable: #만약 배열에서 찾는다면 O(N)인데 
            # hash에서 살펴보니까 O(1)이 됨.
            # list검색 : O(N)
            # hash 검색 : O(1)
            if i == target - i: # 두 키가 같으면 안 돼...! 
                # 키 중복 절대안돼! 
                continue
            else:
                answer.append([i, target - i])
        else:
            print("없어!")

print(answer)
# 자... 하지만 7 7을 썼어... 같은 원소 2번쓰면 안 돼..!!! 
