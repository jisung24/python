N, X = map(int, input('').split(' '))
A = list(map(int, input('').split(' ')))
answer = []
for i in range(0, len(A)):
    if A[i] < X:
        answer.append(A[i])

print(' '.join(str(s) for s in answer))