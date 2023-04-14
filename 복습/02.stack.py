# 스택 
# 그냥 list로 구현하면 돼! 

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# stack.pop()
# stack.pop()
print(stack)

# 가장 최근의 원소! 
print(stack[-1])

stack2 = []
if not stack: 
    # 비어있는 list는 False를 반환.
    # not False여서 True
    # not은 자바스크립트 !이다!!!!!!
    # 그냥 암기! => 비어있는 지 아닌 지 if문에서는 바로 not으로 검사가 가능하다! 
    print("dwdwd")
else:
    print("비어있음!")

# 안에 있는 지 검사! 
stack3 = [1,3,5,7]
print(4 in stack3) # False : 훨씬 더 직관적이다! 
print(4 not in stack3) # True 