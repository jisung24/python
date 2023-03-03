N = int(input())
A = list(map(int, input().split(' ')))
answer = []
answer.append(min(A))
answer.append(max(A))


print(" ".join(str(num) for num in answer))