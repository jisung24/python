# 공식 
# (n/k)
# n! * k!(n - k)!분의 1 
import math
n, k = map(int, input().split())


print(math.factorial(n) // (  math.factorial(k) * math.factorial(n - k)   ))


