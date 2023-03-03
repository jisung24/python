num = int(input())

def printMultiplicationTable(number):
    answer = ''
    for i in range(1, 10): # 1에서 10 - 1까지;
        # 1에서 9까지가 정해져있다면 그냥 range앞에 적어주자..! 
        answer += f"{number} * {i} = {number * i}\n"


    return answer

print(printMultiplicationTable(num))



