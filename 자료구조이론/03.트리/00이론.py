# 트리 
# 🔹 용어정리 🔹
# 1) 노드 : 각각의 데이터를 보관하는 트리의 동그란 공간 
# 2) 간선 : 노드들을 잇는 선
# 3) 루트노드 : 노드 중 가장 최상위에 있는 노드 
# 4) 부모 자식 형제노드 
# 5) 리프 노드 : 자식노드가 더 이상 없는 노드
# 6) 노드의 차수 : 각 노드에서 뻗어나온 간선의 개수 (즉, 자식의 개수와 같다)
# 7) depth : 루트에서 특정 노드까지 가기위해 거쳐야하는 간선의 수 

# ⭐️ 트리가 될 수 있는 조건 ⭐️

# 트리 
# 정의 : 한 개 이상의 노드로 이루어진, 사이클이 없는 연결그래프
# -> 무조건 1개 이상의 노드(루트겠지..?)로 이루어져야 하고, 
# -> 사이클이 없어야 한다..! 
# ❗️조금 이상한 모양도 트리로 내가 만들 수 있어야 한다❗️
# => 🔴 하나 이상의 노드(즉, 간선은 없어도 됨) + 사이클이면 트리 돼 🔴
# => 그리고 노드끼리 끊기면 안 돼!!!!!! (간선이 있다면 무조건 이어져 있어야 돼! )
# => 이 세 가지면 돼! 
# 1. 노드가 1개 이상 있음 
# 2. 간선이 끊어지지 않음 
# 3. 싸이클이 돌지 않는다 

# 트리가 될 수 없는 구조 
# 1. 노드끼리 싸이클이 존재함
# 2. 끊어져 있음 


# ⭐️ 트리는 어디서 사용되는가? ⭐️
# -1) 자료들을 계층적으로 나타내야 할 때! 
# ex) 스포츠 대진표, 컴퓨터 디렉토리, 가족 관계도, 회사 조직도.. 등등


# ⭐️ 트리의 성질 ⭐️
# -1) 노드의 개수는 간선의 개수보다 1개 더 많음! 
# 데이터가 4개이면 간선은 3개이다! 
# -> ❗️사이클이 없기 때문이다..!❗️ 


# ⭐️ 트리의 종류 ⭐️
# 트리에서 하나의 노드는 자식을 0개 1개 2개 3개 4개... 계속 가질 수 있다.
# 하지만 0 1 2개까지만 갖는 트리를 우리는 이진트리 라고 한다. 

# 👉 이진트리 (binary Tree)  
# 높이를 잘 보면 시간복잡도를 알 수 있음
# 2진트리에서 노드의 개수가 4개라는 건... ❗️높이가 3부터 시작함❗️ 
# 최대 7개까지 높이가 3이 될 수 있음! 

# 👉 balanced binary tree(밸런스가 잘 잡힌 이진트리)
# - 양쪽으로 골고루 밸런스가 잘 잡힌 이진트리 

# 👉 unbalanced binary tree(한 쪽으로만 치우친 이진트리) 
# - 한 쪽으로만 계속 내려가는 이진트리
# - ❗️너무 비효율적이다❗️
# - 높이가 N(데이터의 개수)이기 때문이다..


# 👉 완전 이진 트리 
# 이진트리(자식개수 0 1 2)인데 마지막 노드가 무조건 왼쪽부터 채워져 있는 트리 

# 👉 포화 이진 트리 
# 리프 노드를 제외하고는 모든 노드의 자식 노드가 2개인 트리를 의미한다. 


# 👉 이진 (탐색) 트리 (왼쪽자식 < 부모 < 오른쪽자식)
# 이진 트리인데 탐색을 위한 트리 
# -> 왼쪽 자식은 부모보다 작고, 오른쪽 자식은 부모보다 크다. 
# -> 그래서 만약 부모보다 작으면 왼쪽만 탐색하면 돼!!!!!! 
# 그래서 오른쪽은 수행을 안 해도 돼서 ❗️n이턴 탐색 시간을 log로 줄여준다❗️
arr = [5,11,12,14,15,18,19,21,23,25,27,28,29,30,32,37]
# 여기서 27을 찾는 방법 
# 이진 탐색 트리로 하게 되면... 
# 만약 데이터가 찾는 값 보다 작다면 오른쪽으로 더 큰 값을 향해 이동하고,
# 지금 노드가 찾는 데이터보다 크다면 노드보다 더 작은 값으로 즉, 왼쪽을 향해서 이동하면 된다. 
# ❗️오른쪽 왼쪽 다 뒤지는 것보다 절반의 시간이 소요된다❗️
# ❗️중복된 값이 들어갈 수 없다!!!!!!!❗️

# 👉👉 이진 탐색 트리 삽입 
# 만약 삽입 하려는 값이 노드보다 작다면 왼쪽, 크다면 오른쪽..! 
# 🔴 이진탐색트리에서는 중복값을 다루지 않는다 🔴

# 👉👉 이진 탐색 트리 삭제
# -1) 만약 지우고 싶은 노드의 자식이 없는 경우 : 그냥 지우면 돼! 
# -2) 지우고 싶은 노드의 자식이 1개인 경우 : 자식이 지워진 부모를 대체하면 돼! 
# -3) ❗️2개인 경우 : 큰 노드들 중에서 가장 작은 것을 찾아서 대체시킨다.... => 잘 이해 안갔어... 

# ⭐️ << 힙 >> : 이진트리의 종류 중 하나임 이것도 마찬가지로.. 이진 탐색 트리, 완전이진트리, 포화 이진트리...등등 
# 부모 노드의 값이 자식 노드의 값 보다 크거나(작거나) 같다(같은 데이터를 다룬다 => 이진 탐색 트리에 비해서)
# 종류 : 최대힙, 최소힙 
# 최대힙 : 부모 노드의 값이 자식 노드의 값보다 항상 크거나 같다  (부모가 자식보다 크거나 같아)
# 최소힙 : 보모 노드의 값이 자식 노드의 값보다 항상 작거나 같다. (부모가 작거나 같아.. 모든 자식보다)
# ❗️힙은 완전 이진트리 or 포화 이진트리를 만족해야 한다❗️

#### 힙 정리 ####
### ❗️걱정마 파이썬은 라이브러리가 있어❗️ ### 
# 무조건 완전 이진트리 or 포화 이진트리를 만족해야 한다.  (머릿속에 그림을 그리자!)
# -1) 최대 힙 : 자식보다 부모가 항상 크거나 같다.(루트가 가장 큼 => 올라갈 수록 커진다)
# -2) 최소 힙 : 자식보다 부모가 항상 작거나 크다.(루트가 가장 작겠지? => 올라갈수록 작아진다.)

# 힙 단점 
# 자식은 부모보다 크거나(작거나) 같다는 것만 알고있지, 깊게 파고드는 건 알 수 없지..! 
# ❗️그래서 단순 크기만을 비교할 때 사용된다❗️



# 🔴🔴🔴🔴🔴🔴🔴🔴 이진 탐색 트리 vs 힙 🔴🔴🔴🔴🔴🔴🔴🔴

# 이진 탐색 트리 
# -1) 왼쪽 자식은 부모보다 작고, 오른쪽은 더 크다 
# -2) ❌ 그래서 중복된 자원을 허락하지 않는다 ❌
# -3) 정렬된 상태를 유지한다(왼쪽 < 부모 < 오른쪽 항상 유지 => 중복x기때문에 <=는 없음) 
# -4) 정렬이 돼 있기 때문에, 특정 노드에 대한 접근이 가능하다. 

# HEAP (완전 이진트리 or 포화 이진트리 + 부모가 자식보다 항상 크거나(작거나) 같다)
# - 정렬이 되어있지 않기 때문에, 특정 노드에 대한 접근이 불가능하다. 
# - 가장 크거나 가장 작은 원소는 root이기 때문에 O(1)을 가진다. 
# - 중복값을 허용한다. 

# 🔴 트리 알고리즘 🔴
# 힙에서 최댓값, 최솟값 구하기 (최대힙의 root 최소힙의 root 구하면 O(1)이면 구할 수 있음) => 단 heap으로 만드는 데 O(N)이 걸림 


# ⭐️ 이진트리 순회 방식 ⭐️
# 👉 전위 순회 (Pre Order)
# - 탐색 순서가 (부모 -> 왼쪽 싹 -> 오른쪽 싹)

# 👉 중위 순회 (In Order)
# - 탐색 순서 ()

# 👉 후위 순회 (Post Order)
# 👉 레벨 순회 (Level Order)
