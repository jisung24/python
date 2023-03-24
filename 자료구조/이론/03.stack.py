# 스택은 그냥 list로 구현하면 끝이야! 

arr = [1,2,3,4,5]
stack = []
while len(arr) > 0:
    stack.append(arr.pop())


print(stack)