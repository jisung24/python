# 문자열이 나오면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램! 
N = int(input())
answer = ''
# 단순 3번 반복이니까 변수를 없애준다! (단순 반복이라는 힌트이다!)
for _ in range(N):
    string = input()
    # 문자열 인덱싱을 묻는 문제! 
    answer += (string[0] + string[-1]) + '\n'

print(answer)