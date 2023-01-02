# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 저기서 입력값을 동일한 index값을 뺴주면 값이 나와!

# python배열 = 리스트
chess = [1, 1, 2, 2, 2, 8]
# print(f"type >> {type(chess)}") # <class 'list'>
king, queen, look, b, knight, pone = input().split(' ')
inputArr = [king, queen, look, b, knight, pone]

# 전형적인 for문
for i in range(0, len(chess)):
    print(f"{chess[i] - int(inputArr[i])}", end=" ")
