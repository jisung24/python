# 1. 스택에 쌓이는 조건 
# => N이 나올 때 까지 쌓인다.

# 2. 스택에서 pop이 되는 조건 
# => 쌓이는 수가 N이 되면 빠져나간다! 
# => 그렇지 못 하면... 수열이 될 수 없다./!! 

# ex)괄호 => 쌓이는 건 열리는 괄호만 
# ex)pop은 바로 앞에 값만 보고 판단을 한다. 

N = int(input()) # 8을 입력받ㅇ므
count = 1
answer = ''
stack = []

for i in range(N):
    
    data = int(input()) # 숫자를 입력을 받아..! 

# push가 될 조건 
    while count <= data: # 4 
        stack.append(count)
        answer += '+' + '\n'
        count += 1

    # 5가 됨 
    # count는 5가 돼도 stack에는 4까지 쌓임! 
    # count가 5라는 건 4까지 했고 다음 차례가 5다! 라는 의미 정상적인거야 
    if stack[-1] == data:
        stack.pop()
        answer += '-' + '\n'
    else:
        print("NO")
        exit(0) # 프로그램 자체가 종료 
        # break는 반복문을 빠져나가기 위함 
        # 하지만 exit는 그냥 반복이고 뭐고 프로그램 자체를 꺼버린다. 


print(answer)



# (숫자 배열 생성) => 큰 숫자까지 가면 시간초과 남 
# 시간복잡도 잡아먹은 원인 숫자배열 생성 유력...! 

# count하는 방식으로 해야 시간초과가 나지 않음 
# 