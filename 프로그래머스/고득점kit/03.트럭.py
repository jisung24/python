from collections import deque 
bridge_length = 100
weight = 100
# 10kg까지 버틸 수 있고, 올라올 수 있는 트럭 개수는 최대 2개이다. 
# 3개째에서 조건문을 써줘야 돼..! 
wait = deque([10,10,10,10,10,10,10,10,10,10])
crossing = deque(weight * [0]) # 0 100개로 초기화하는 방법...! 
finished = []
sum = 0
time = 0
while True:
    # crossing으로 이동할 조건..!
    if len(crossing) <= bridge_length and sum <= weight and wait:
        # wait도 남아있어야 돼..! 
        # 남아있지 않으면 crossing으로 이동할 수 없어...! 
        sum += wait[0]
        # 0이 나가고 숫자가 들어와야 한다...! 
        crossing.popleft()
        crossing.append(wait.popleft())
        time += 1
    else:
        # crossing으로 이동을 못 해주니까 
        # crossing에서 지금 지난 트럭까지 옮겨줘야 돼...! (숫자를)
        # 근데 숫자를 pop시키고 싶은데 앞에 0이 있어...! 
        # 다 제거해줘야 돼
        # 지금 앞에 0이 많고, 계속 뒤에 숫자가 쌓여서
        # 더 이상 숫자는 못 쌓고 0을 제거해주고 숫자도 내보내줘야 돼..! 
        if not crossing:
            break
        else:
            # 숫자가 나올 떄 까지 다 뺴줘야 돼... 0을! 
            try:
                while crossing[0] == 0:
                    crossing.popleft()
                    time += 1
                # 다 뺐으면... 
                sum -= crossing[0]
                time += 1
                finished.append(crossing.popleft())
                if not crossing:
                    break
            except:
                pass
print(time)



##### 아 대박.... 
# 이거 다리를 한 번에 빠져나가는게 아니라........
# bridge_length만큼 길이가 있는거야...
# 예를들면 length가 2면 2번 pop이 돼야 나갈 수 있어...! 




