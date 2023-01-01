# input함수
# - return값이 무조건 문자열이야.. => 그래서 숫자 입력받을거면 무조건 형변환 함수 써줘야 해!
# - 형변환 함수 : int(), float(), str(), char(), bool()

# 1. 문자(열) 입력받기

# name이라는 변수 안에 input의 return값을 넣어줌 => javascript에서도 많이 쓰는 방식!
# let name = () => 3 ( name이라는 변수에 3을 넣는거야! )
name = input("이름을 입력해주세요 >> ")
print("입력받은 이름 >> ", name)
