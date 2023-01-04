# x or y가 0이라면 어떤 사분면에도 속하지 않아!
x = int(input())
y = int(input())

if (x or y) == 0:
    print("어떤 사분면에도 속하지 않습니다!")
else:
    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("4")
