# 왜 큐인지? => 순서대로 지정한 대로 나가야하니까! 
# 맨 앞 숫자가 100이 될 때 까진 나가지 못 하고 계속 큐를 순회해야 돼! 
from collections import deque 

progresses = [93, 30, 55]
speeds = [1, 30, 5] 
# 같은 index끼리 큐를 돌면서 계속 더해줘야 돼!! 
proQueue = deque(progresses)
spQueue = deque(speeds)
answer = []
# 그냥 넣어주면 되네...

i = 0
# 애초에 while문에 남지 않으면 들어오질 못 하는데....? 

while len(proQueue) != 0:
    # proQueue의 길이가 0이 아닐 때 계속 반복! 

    # 1. 체크를 한다
    if proQueue[0] < 100:
        # 100보다 작다면...! 계속 100이 될 때 까지 돌아준다.! 
        # 3바퀴씩 돌려준다! 
        for j in range(len(proQueue)):
            # 3번 무조건 고정..! 
            proQueue[0] += spQueue[0]
            # 어차피 앞에 있는 게 계속 뒤로 가니까 0번만 3번 더해주면 돼! 
            proQueue.append(proQueue.popleft())
            spQueue.append(spQueue.popleft())
        # 3번 반복을 돌려줘..! 
        # print(spQueue, proQueue)
    else: 
        # 즉, 맨 앞 수가 100이 되면 여기까지 잘 와..! 
        count = 0
        # print("맨 앞 수 100 됐습니다...=~")
        # print(proQueue, spQueue)
        while proQueue[0] >= 100:
        # 아... 다 나가고 나서 빈 큐인 상태에서 while문을 한 번 더 두들기는데... 이때 Index로 접근해서 그런 거 같아...! 
            # 그니까 끝나기 전에 len이 0이면 break를 해주면 돼! 
            proQueue.popleft()
            spQueue.popleft()
            count += 1
            if len(proQueue) == 0:
                break
        answer.append(count)

print(answer)