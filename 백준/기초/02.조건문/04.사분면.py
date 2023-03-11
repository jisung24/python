x = int(input('x좌표 >> '))
y = int(input("y좌표 >> "))

def checkQuadrant(dotX, dotY):
    # 잘 보면 x와 y는 0이 주어지지 않음. 
    if 0 < x and y > 0: # 둘 다 양수라면! 
        print(1)
    elif x > 0 and y < 0: # 4
        print(4)
    elif x < 0 and y > 0:
        print(2)
    else:
        print(3)


checkQuadrant(x, y)