## 더하기 사이클 ## 
# => 더해서 다시 원래대로 돌아온다...! 

N = int(input())

P = N # P는 26을 유지한다...! 
i = 0
# print("8".zfill(2)) => 08

while True:
    # 1번째 step
    # N을 계속 바꾸고 반복하는거야...! 
    i += 1
    arrList = list(map(int, list(str(N))))
    # print(arrList, type(arrList[0])) # 5 5

    total = sum(arrList) # 10 


    N = arrList[len(arrList) - 1] * 10 + (total % 10)
    if N == P:
        break

print(i)