# key만 알면 어디에 저장이 되어야 하는지, 어디에 있는 지 바로 알 수 있다. 
# python으로 hash구현 


# ⭐️ hash table(찾는 것 O(1)) ⭐️
# - key에 데이터를 저장하는 data구조 
# 👉 장점 
# key를 통해 data를 바로 찾을 수 있어서 찾는 속도가 O(1)임 
# -- 배열에선 O(N)임 훨씬 빠름

# 예시 
# 배열에서 값을 하나 찾으려면 index 0번 부터 다 뒤져가면서 순차 탐색을 해야함 
# 최악의 경우, 값이 없을 수 있고, 가장 뒤에 있을 수 있어. 

# 하지만 hash는 key만 입력하면, 그 데이터가 어디에 있는지, 아니면 없는 지 
# 바로 알 수 있어! 
# 즉, 키 이름으로 바로 O(1)만에 바로 알 수 있음 
# 왜냐면 hash함수가 key를 보자마자 어디에 들어가야 하는 지 바로 알려주기 때문에 ,
# 그 자리로 이동을 함. (충돌이 일어날 순 있음)





# 👉 해쉬 함수 구현 
# 파이썬 딕셔너리 타입이 hash table구현 

def hashFunction(key):
    address = key + 131313
    return address
# 위와 같은 식으로 구현한다. 
# 👉 hash function 
# key를 넣으면 그냥 어디에 들어갈 지 주소값을 return해주는 함수 

# 요약 
# hash는 배열의 찾기 단점을 바로 감싸줌 O(1)
# hash함수가 데이터가 어디에 있는 지 바로 알려주기 떄문 
# 구현은 dictionary로 돼 있다. => 구현할 필요없어. dic 자체가 hash임

