import sys
# count함수로 배열에서 해당 수 개수를 파악하기! 
# 계속 말 하지만 만약 모든 수의 개수를 다 파악해야한다면 hash를 사용하는 게 훨씬 좋음. 
tc = int(sys.stdin.readline())
lists = map(int, sys.stdin.readline().split(" "))
find_num = int(input())

print(list(lists).count(find_num))


