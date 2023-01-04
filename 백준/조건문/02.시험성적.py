# 조건이 너무 많을 때는 switch case사용하는 것도 나쁘지 않아..
# 계속 elif elif ~~ 쓰면 너무 길어짐.
# 하지만!! python에서는 switch문이 존재하지 않아.❗️

# score = int(input("시험 성적 >> "))

# if (score >= 90 and score <= 100):
#     print("A")
# elif (score >= 80 and score <= 89):
#     print("B")
# elif (score >= 70 and score <= 79):
#     print("C")
# elif (score >= 60 and score <= 69):
#     print("D")
# else:
#     print("F")
# ⭕️ 파이썬은 if조건칸에 괄호 안 침!

score = int(input())

if score >= 90:  # 조건1
    print('A')  # 조건1이 참인경우
elif score >= 80:  # 조건2
    print('B')  # 조건2가 참인경우
elif score >= 70:  # 조건3
    print('C')  # 조건3이 참인경우
elif score >= 60:  # 조건4
    print('D')  # 조건4가 참인경우
else:
    print('F')  # 위 모든 조건이 거짓인 경우

# 이렇게 조건이 많다면 삼항연산자는 안 쓰는게 좋아보임
# 코드 짧게 쓰려고 쓰는건데 간단한 조건식에 써야 짧아보이지...
# 이렇게 조건이 많다면, 삼항 연산자가 오히려 조금 가독성도 떨어지는 것 같아보임.


# 요약
# 1. python에는 switch문이 존재하지 않는다.
# 2. else if가 아닌,, elif로 단축해서 사용한다.
# 3. ❗️if문 다음 실행문장은 들여쓰기를 해줘야한다.
# 4.
