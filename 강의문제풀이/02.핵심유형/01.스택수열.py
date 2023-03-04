stack1 = []
stack2 = []
answer = []

# N : stack에 들어갈 원소의 수! 1부터 N까지의 원소가 stack에 담긴다(중복x)
N = int(input())

# stack1은 그냥 8부터 쌓여서 1까지...의 수가 들어감! 

for i in range(N, 0, -1): # 2번째 수 앞에까지.. 그니까 1까지 옴 
    stack1.append(i)


# 이제 본격적으로 입력을 받을 차례야...! 

for i in range(8): # 8번 입력받음...!  
    M = int(input())
    if len(stack2) == 0: # stack
        while True:
            # M이 될 때 까지...계속 
            # stack1.pop()한다 만약 pop한 값이 4라면 
            # append(pop())한다. 
            stack2.append(stack1.pop())
            if stack2[len(stack2) - 1] == M:
                # 만약 4라면...
                answer.append(stack2.pop())
                break
    else:
        if M == stack2[len(stack2) - 1]:
            answer.append(stack2.pop())
            break
        elif M > stack2[len(stack2) - 1]:
            # M이 나올 때 까지... 계속 stack2에 넣어준다...! 
            stack2.append(stack1.pop()) 
            if(stack2[len(stack2) - 1] == M):
                answer.append(stack2.pop())
                break

