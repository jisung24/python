# for i in range(1, 10, 2): 
# 파이썬의 for문은 for 변수 in ~ 으로 이루어짐 
# in뒤에 있는 여러 숫자, list, 문자열, 튜플이 전부 올 수 있다. 
# 근데 저 in 뒤에 있는 저 자료형들의 자료를 1개씩 i가 순회한다. 

# 요약 
# for 변수 in [반복문 돌릴 대상이라고 생각하자!(리스트, 튜플, 문자열) ] 
# for~in이 세트야! 
# 저 변수에 반복문 돌릴 대상의 원소들이 1개씩 들어감. 
# for 하면 무조건 in을 떠올려보자


# 유용한 함수 
# sum(배열이름) : 배열의 합을 구할 수 있음 
# len(배열이름) : 배열의 길이를 구할 수 있음 
# list.count("원하는 원소") : 원하는 원소의 개수를 알 수 있음 => hashmap에서 value구할 때 많이 사용됨.
# 


arr = [1,2,34]
print(arr[::-1]) # 역으로 슬라이싱 한다! => 꿀팁! 
listValue = [1,2,3,4,5] # list(range(5)로 생성 가능
 
revArr = listValue.reverse()
print(revArr) # reverse는 원본을 뒤집어주지 그걸 return을 하지 않는다. 
# reverse를 단독으로 사용하고 원본을 출력해줘야한다! 
# [::-1]로 슬라이싱을 하던가! 
print(listValue)