# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# ==> 약간 연산자 우선순위 따지는 문제같음. => 중요한 것만 알면 돼! 다 외울 필요는 없어.

num1, num2, num3 = input().split(' ')

print(f"{(int(num1) + int(num2)) % int(num3)}")
print(f"{((int(num1) % int(num3)) + (int(num2) % int(num3))) % int(num3)}")
print(f"{((int(num1) * int(num2))) % int(num3)}")
print(f"{((int(num1) % int(num3)) * (int(num2) % int(num3))) % int(num3)}")
