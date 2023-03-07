# 수는 무조건 2자리 수!! 
N = int(input()) # 정수 1개 입력받음...
Q = N # 나중에 Q와 비교한다.

i = 1
while True:
    # 1스텝 : 각 자리의 숫자를 더한다. => 합의 오른쪽과 sum % 10을 붙인다! 
    first = list(map(int, list(str(N)))) # [2, 6]

    # step 2 : 
    # 68을 만든다...! 
    second = first[len(first) - 1] * 10 + (sum(first) % 10)
    N = second 
    print(f"N >> {N}")
    if N == Q:
        print(f"{i}번 함!!")
        break
    i += 1 # 1번 끝...! 
