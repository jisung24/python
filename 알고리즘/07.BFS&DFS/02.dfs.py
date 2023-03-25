# 마찬가지로 그래프 탐색이야 그냥! 
# ⭐️ 어떻게 탐색을 하냐의 차이야 ⭐️

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

# 탐색 방향 왼쪽 오른쪽은 상관없어! 
# 코드 진짜 똑같아! 한 두 줄만 다른거야...! 
def DFS(graph, start):
    visited = list() # stack은 그냥 list면 돼! 
    need_visit = list() 

    need_visit.append(start) 
    while need_visit:
        node = need_visit.pop() # stack에서! 
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(DFS(GRAPH, 'A'))