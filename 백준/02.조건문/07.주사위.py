dice1, dice2, dice3 = map(int, input().split(' '))

# 이거 hash로 풀 수 있어
# 각각의 눈이 몇 개 인지 적어주자.!!  

diceArr = [dice1, dice2, dice3]
setDice = list(set(diceArr))
dic = {}

for i in range(len(setDice)):
    dic[setDice[i]] = 0

for i in range(len(diceArr)):
    if diceArr[i] in dic:
        dic[diceArr[i]] += 1

keys = dic.keys()
# print(len(keys)) => 2
def get_key(val):
    for key, value in dic.items():
         if val == value:
             return key
 
    return "There is no such Key"

def check_money(keys):
    money = 0;
    if len(keys) == 1:
        money += (10000 + (diceArr[0] * 1000))
    elif len(keys) == 2: # 겹치는게 2개이다...! 
        # 값이 2인 key를 찾아서 하면 된다. 
        # items사용하기
        findKey = get_key(2) # 값이 2개인 key를 찾아와라...! 
        money += (1000 + findKey * 100)
    else:
        # 배열에서 가장 큰 max 구하기
        money += (max(diceArr) * 100)

    return money

print(check_money(keys))



# 몇 개인 지 묻는 문제가 나올 때 hash => 각각의 주사위의 개수를 알 수 있어