# last in first out 성격 100% 활용하기 
# 1. 일단 first out이란 게 있으려면 일단 뭐가 append가 돼야돼! 
# append가 되는 조건 따져보기

# 2. 이제 꽃 first out 조건 살펴보기! 
# => 이 조건 잘 짜면 끝나 

# 정리 
# 일단 원소가 들어가야 돼! => 그래야 first out이 될 수 있어
# stack에 push조건을 생각하기 

# 가장 stack의 마지막에 있는 원소가 못 나오면 끝이야(❗️그래야 first out속성을 이용하는거야! )
# 그래서 마지막에 있는 원소와 비교해서 나오게 하면 돼! 


# 1. push 조건을 따져보고 값을 무조건 push를 시켜주기 
# 2. LIFO의 특징을 따져주기 위해서 일단 pop조건을 따져주기 
# push, pop조건을 나눠서 생각을 해보자! 
# ❗️pop조건은 쉬워 그냥 stack의 마지막원소와 연관 지어주면 돼❗️
# 괄호.. 짝이 맞는 지 검사하기 


# push 조건 : "여는 괄호가 나와야 한다"
# pop 조건 : stack의 마지막 원소와 짝이 맞아야한다. 
bracket ="(((((()))(())(())))"

def isTrue(bracket):
    stack = [] # 빈 스택 생성 
    for i in bracket:
        if i == "(":
            # 스택에 쌓아줘야 last in first out이 가능함 
            stack.append(i)
        else:
            if not stack:
                # 스택이 비어있다면...! 
                # first out 할 게 없어..... 
                return False 
            else:
                stack.pop() # last in first out 
    # 반복문 다 돌리고 나옴 
    if stack:
        return False
    else:
        return True


print(isTrue(bracket))