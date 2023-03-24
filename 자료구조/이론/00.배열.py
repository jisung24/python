# 배열 
# 파이썬에선 list라고 해서 실제 배열보다 많은 기능을 제공하고 있음 

# 정의
# 👉 같은 종류의 자료들을 모아놓을 수 있는 자료구조 
# 👉 당연히 자료들이 여러군데 흩어져 있는 것 보단 모아져 있는 게 좋음 
# 👉 스타에서도 서플라이 여러 군데에 막 지으면 더럽잖아...! => 이쁘게 지어야지 
# 👉 ❗️각 자료의 순서대로 index라는 게 부여가 됨❗️
# 🔴 정리 : 각 자료들을 모아서 저장할 수 있고, 각 자료들에게 index번호, 위치번호가 부여가 돼서 1로 접근이 빠르게 가능함 🔴

# 장점 
# 1. Random Access : 빠른 접근이 가능하다 O(1)로 접근이 가능 
# -> 인덱스 0번이나 10000000번이나 접근 속도가 같다. 
# -> 인덱스 번호가 부여돼서 ❗️(바로 맨 앞 주소)❗️  * 띄워진 거리 로 한 번의 연산이 가능하기 떄문

# 단점 
# -1) 추가 시 사이즈 문제 : 할당 전 고정된 크기를 미리 할당을 해 줘야해서, 중간에 예상치 못 한, 
# 데이터 초과 시 다시 새로운 배열을 할당해줘야 한다. 

# -2) 중간, 앞 삭제 O(N) : 중간이나, 처음을 삭제 할 시, 
# 빈 공간이 생겨서 그 공간을 없애기 위해 원소들을 전부 이동시켜줘야 함! 
# ❗️값 1-2개 바꾸기 위해서 모든 원소들이 싹 다 칸 이동이 필요하다❗️

# -3) 중간, 앞 삽입 O(N) : 삽입을 하려면 공간을 만들어줘야해서, 
# 다시 그 뒤에 있는 원소들을 한 칸씩 뒤로 이동시켜줘야 한다. 