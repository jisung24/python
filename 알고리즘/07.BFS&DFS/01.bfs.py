# 그래프 탐색 알고리즘 
# 일단 같은 level먼저 지그재그 식으로 탐색하는 알고리즘 

# 1. 방문 안 한 queue (need_visit)
# 2. 방문이 끝난 queue (visited)

# 즉, 큐에 넣고 꺼내는 형식으로! 
# 즉 need_visit이 비어있다면! => 더 이상 탐색할 노드가 없다면~ 
from collections import deque

GRAPH = {
    'A' : ['B', 'C'], # A정점과 연결 돼 있는 정점은 BC이다.
    'B' : ['A', 'D'], 
    'C' : ['A', 'G', 'H', 'I'],
    'D' : ['B', 'E', 'F'],
    'E' : ['D'], 
    'F' : ['D'],
    'G' : ['C'],
    'H' : ['C'],
    'I' : ['C', 'J'],
    'J' : ['I']
}

# ⭐️ 외워야 함 ⭐️
# ⭐️ BFS DFS 둘은 무조건 외워야 함 ⭐️
# ⭐️ 그래프 탐색 방법이야 그냥 ⭐️
def BFS(graph, start):
    visited = deque() # 방문이 필요한 큐
    need_visit = deque() # 방문이 다 끝난 큐

    need_visit.append(start) # 시작 노드를 하나 넣고 시작한다.

    while need_visit: # 방문이 필요한 노드가 더 이상 없을 때 까지
        # 방문할 노드가 더 이상 없을 떄 까지! 
        node = need_visit.popleft() # 나갈 노드를 하나 걸어놓는다. => 객체에 나가는 노드와 연결돼 있는 노드를 접근해줘야 하기 때문이다. 
        if node not in visited: # 만약 방문이 끝난 노드에 node가 있다면 넣어주고, 아니면 그냥 버린다(위에서 바로 popleft를 해 준 이유이다.) 
            visited.append(node) # 방문이 끝난 노드에 넣어준다 
            need_visit.extend(graph[node]) # 그 노드와 연결된 값들을 한 번에 큐로 넣어준다. 

    return visited # 방문이 다 끝난 노드를 return한다. 


print(BFS(GRAPH, 'A'))

