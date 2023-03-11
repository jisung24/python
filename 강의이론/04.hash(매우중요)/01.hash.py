# 어떤 상황에서 hash를 사용하는지 매우 중요하다 
# ❗️ hash를 어느 상황에서 사용하는지 ❗️

# 구현 법 
# 1. array list(파이썬 list)
# 2. array + linked 둘 다! 

# ❗️파이썬에서는 array list로 구현을 해 놓아서 굳이 2번은 사용하지 않을거야❗️
# 이제 우리가 집중해야 할 내용은 hash를 어떤 상황에서 쓰는 지! 

# 실제 코딩테스트에서 어떻게 hash를 활용할지! 
# array list로 구현을 했으면 open addressing으로 충돌을 막는다(코테에선 쓸모없음 면접에서만..!)

# ⭐️ 내용 이해 ⭐️
# 1. 우리는 key value쌍으로 array list에 저장할거야(배열로 구현)
# 2. 그럼 name = "지성"은 몇 번째 index에 저장이 될까? 
# 👉 name이란 key를 hash function에 넣어준다. => 그럼 hash function이 index를 return해주는데, 거기다가 넣어줘
# ❌ 자 그럼 그냥 굳이 hash함수 사용 안 하고 key값을 index로 사용하면 되는 거 아니야? => direct-address Table
# 근데, key값으로 문자열을 받으면? => 몇 번째 index에 어떻게 들어갈 수가 없어.
# 그래서 hash가 나온 거..! => function에다가 가공을 해서 나온 값을 Index로 지정한다. 
# hash function은 나오는 index의 범위가 정해져있어 => ex) 0 - 9번까지

# ❗️즉, 어떤 key가 들어오더라고 주소값을 변환을 해줘서 들어갈 수 있다!!!!!  
# 그래서 hash function을 통해서 index값을 정하는 자료구조를 hash table이라고 한다. 
# 자 그럼 hash함수는 무적이야...? => ❗️아님❗️
# ❗️서로 다른 자료에 대해서 같은 index를 반환해줄 수 있어❗️

# 해결책 2가지 
# array list : open addressing (충돌나면 한 칸 옆으로 가는 거!)
# 또 충돌이 나면 계속 한 칸 옆으로 감( 한 번에 몇 칸 가는 지는 다양하다 )

# 우리는 잘 구현된 hash function이 있음 
# 우리가 key값에 해당되는 index로 찾아가는 과정이 O(1)이다 
# 파이썬에서는 hash가 dictionary로 잘 구현이 돼 있다. 