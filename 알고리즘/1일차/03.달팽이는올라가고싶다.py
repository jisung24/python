# 높이 : V
# 낮에 : A
# 밤에 : -B 
# 현재 높이 : height 

# 한 번 이라도 V에 도달하면 끝..! 

# height = 0
# A, B, V = map(int, input().split())

# # 우선 좀 무식하게 푼다..!

# i = 0
# while True:
#     i += 1
#     height += A
#     if height >= V:
#         print(i)
#         break
#     else:
#         height -= B
    


# 시간 복잡도가 너무 길어...! 
# 공식으로 풀던가 이분 탐색으로 풀어야 해
# N의 크기가 1억이야... => n으로도 풀면 안 돼! 

# 5에 가기 위해서 
# 2씩 올라간다..
# 근데 5에 도달을 못 했으면 1을 내려가야 한다. 

# 5에 도달하려면... 




print(i)