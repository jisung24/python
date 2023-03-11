# queue는 list(어레이리스트)구현 시 pop을 할 때 O(N)이 소요가 됨 
# 그래서 linked list로 구현했음 


# 근데 stack은 가장 끝에서 push pop이 일어나기 때문에,
# array list로 구현해도 push pop 둘 다 O(1)이어서 그냥 list로 구현하면 끝! 

# stack
# 👉 가장 최근에 추가한 자료가 가장 먼저 나가야함! (그래서 pop 할 때 가장 마지막 원소가 나가지 못 하면 끝이야...)
# ❗️그래서 가장 끝에 있는 원소랑만 비교해서 pop하면 끝이야❗️


# list (array list)로 스택 구현 
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)

print(stack)

stack.pop() # last in first out 
stack.pop()
stack.pop()