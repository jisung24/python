# ⭐️ 트리 (계층구조)
# 어디에 사용되나? 
# 1. 월드컵 대진표
# 2. 회사 조직도
# 3. 가족 관계도

# ⭐️ 트리 정의 ⭐️
# (1개 이상의)노드와 브랜치를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
# 방향 그래프의 일종이다(위에서 아래로) 
# 노드끼리 즉, 상하관계가 지어진거야..! => 그런 자료구조야! (상 하 관계 => 부모 자식관계)

# ⭐️ 트리 용어 ⭐️
# 1) 노드 : 트리 구조에서 데이터를 저장하는 공간
# 2) 루트 노드 : 트리에서 꼭 있어야 할 노드(가장 상위에 있는 노드)
# 3) 레벨 : 루트에서 가장 최 하에 있는 노드까지 연결된 간선 개수 
# 4) 부모 노드, 자식, 형제 노드 
# 5) 리프 노드 : 더 이상 자식이 없는 노드 
# 6) 뎁스 : 트리에서 트리가 가질 수 있는 최대 level 
# 7) 차수 : 노드에서 자식의 개수! 


# ⭐️ 트리 종류 ⭐️
# 1) 이진 트리 : 모든 노드의 자식들이 0 1 2명인 트리 
# 2) 완전 이진 트리 : 이진 트리인데, 왼쪽부터 채워진 트리
# 3) 포화 이진 트리 : 리프 노드를 제외하고 모든 노드의 자식이 2명 
# 4) 힙 : 완전 or 포화 이진트리 
# 5) 이진 탐색 트리(BST) : 이진트리에 다음과 같은 조건이 하나 추가된 트리 
# - 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽은 해당 노드보다 큰 값 
# - 그래서 큰 값을 찾으려면 무조건 오른쪽으로 가면 되고, 작은 값을 찾읗려면 무조건 왼쪽 값을 찾으면 돼! 
# 만약 왼쪽 노드 1개만 있다면 더 작은 값이 있어야 하고,
# 오른쪽 노드 1개만 있다면 더 큰 값이 있어야 한다. 

# 그래서 값이 들어오면 그 값을 계속해서 트리에 있는 값들과 비교해서
# 비교하는 값보다 그 값이 크면 오른쪽으로 내려주면 되고,
# 작으면 왼쪽으로 계속 보내주면 돼! 
# 저걸 반복해주면 알아서 위치를 찾게 됨! 
# 즉, 큰거는 오른쪽으로 보내주고, 작은 건 왼쪽으로 보내준다. 
# ❗️단 같은 원소는 없어야 한다❗️

# 👉 사용 용도 : 데이터를 검색 할 때 => 빠르게 찾을 수 있다. 
# 👉 장점 : 검색 속도 개선할 수 있음
# 가장 작은 값은 계속 왼쪽 노드로만 가면 바로 알고,
# 가장 큰 값은 계속 오른쪽으로만 가면 바로 알 수 있음 


# 이진 탐색 트리 구현..! (노드를 만들어서 이진 탐색 트리에 넣어주는 형식)
# 연결리스트로 구현하기 위해서 노드 자체를 class로 만들어준다. 
class Node: # 노드 클래스 
    def __init__(self, value):
        self.value = value # 값 
        self.left = None # 왼쪽으로 내려가기 위해 왼쪽에 있는 그 다음 노드의 주소값 
        self.right = None # 오른쪽 아래에 있는 노드의 주소값 


class NodeMgmt:
    # 처음 들어가는 노드는 무조건 root노드가 됨 (root를 head로 표현했음)
    def __init__(self,head):
        self.head = head

    # 이진 탐색 트리에 값 하나 삽입! 
    # 삽입을 하기 위해선, 적절한 위치를 찾아야하고, 순회를 해야 함.
    def insert(self, value):
        self.current_node = self.head
        # self.current_node : 지금 값을 비교하는 원래 이진 탐색 트리에 있던 노드 
        # self.current_node.left : 탐색하는 트리의 왼쪽 
        # self.current_node.right : 탐색하는 트리의 오른쪽 
        # self.current_node.value : 탐색하는 트리의 값 
        while True:
            if value < self.current_node.value:
                # 원래 이진 탐색에 있던 값보다 작다면 왼쪽으로 가야지! 
                # 작은 값은 왼쪽으로 간다. 
                if self.current_node.left != None:
                    # 만약 탐색하는 노드의 왼쪽이 있다면 
                    self.current_node = self.current_node.left
                    # 비교할 대상을 왼쪽으로 내려가준다! 
                else:
                    # 만약 왼쪽이 없다면 그냥 노드를 만들어서 생성해주면 돼! 
                    self.current_node.left = Node(value)
                    # 노드에 value를 넣어서 그냥 왼쪽 값에 넣어준다. 
                    break
            else: # 같은 경우는 없고, 무조건 value가 더 크다면! 오른쪽으로 가자! 
                if self.current_node.right != None:
                    # 오른쪽에 노드가 있다면...
                    # 그 오른쪽 노드로 비교대상을 바꾼다. 
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    # 특정 data노드가 있는 지 없는 지 확인시켜주는 코드!     
    def search(self, value):
        self.current_node = self.head # 루트 부터 순회하겠다! head값을 대입한다. 
        
        while self.current_node:
            if self.current_node.value == value:
                # 순회하는 각각의 노드가 value가 맞다면!
                return True
            elif value < self.current_node.value:
                # 찾고자하는 value가 더 작다면 왼쪽으로...! 
                self.current_node = self.current_node.left
            else: # 마찬가지로 같은 경우는 없음
                self.current_node = self.current_node.right
            # 만약 none인 경우 while을 벗어난다.

        return False
    # while에서 맞는지 코드를 짜주고, 만약 while에서 안 걸리면 그냥 False를 return한다.

    # def delete(self, value):
         

# 이진 탐색트리 구현 완료! 
# head는 그냥 root라고 생각하면 돼! 
head = Node(1) # 루트 노드를 하나 만들고 
BST = NodeMgmt(head) # 노드를 BST에 넣어줌! 
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
# 여기까지 들어간다. 

# 이제 찾는거! 
print(BST.search(8)) # True 
print(BST.search(100)) # False
print(BST.search(-1)) # False




# 이진 탐색 트리(BST)의 시간복잡도 
# 찾기 :  O(log n) : 개빠름 
# 