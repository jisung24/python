n = int(input())

def sumToN(n):
    sum = 0
    for i in range(1, n + 1): # i가 1부터 n까지이다. 
        sum += i
    return sum

print(sumToN(n))



# print(f"sum >> {sum}") ==> f-string방식 