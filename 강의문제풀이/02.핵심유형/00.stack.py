# 스택 
# 1. 구조를 이해하자 
# - data를 제한적으로 접근한다 => 무조건 한쪽 끝에서만 접근이 가능하다
# - @@@@ 가장 나중에 작업한 data를 가장 먼저 취소할 수 있는 data @@@@ 
# - 예시 : 쌓여있는 책 => 위에 부터 꺼내야 한다. 
# - 큐는 줄서기, 스택은 책 쌓기 라고 이해하면 완벽함.

# 2. 간단한 용어 몇 가지
# - 스택에 data넣기 : push
# - 마지막 원소부터 계속 빼기 : pop

# 3. 파이썬으로 스택 구현하기
# push => append
# pop => pop함수 

stack =  list()

# push 
def push(value):
    stack.append(value)

# pop
def pop():
    return stack.pop() # 빠진 원소 return하기! 

push(3)
push(4)
print(stack)
print(pop())
print(stack)
# 4. 일단 이해를 하고 암기하자 
# - 짝이 맞는지 : 왜 stack인가? : }가 오면 가장 나중에 쌓인 data와 비교해서 쌍이 맞으면 pop시킨다. 
# - 그리고 그런 식으로 검사를 해서 stack이 size가 0이면 짝이 맞는거야. 

# 일단 list로 데이터들을 보관해두고, 각각 작업은 stack에서 하는거야! 

# ⭕ 스택은 가장 마지막에 있는 data를 필요로한다 ⭕