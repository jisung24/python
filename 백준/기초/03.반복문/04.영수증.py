totalPrice = int(input())
countOfType = int(input()) # 물건 종류의 수 

def isRight(totalPrice, countOfType):
    for i in range(1, countOfType + 1):
        item, countOfItem = map(int, input().split(' '))
        totalPrice -= (item * countOfItem)

    print("Yes") if totalPrice == 0 else print("No")


isRight()