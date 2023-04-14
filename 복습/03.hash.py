# hash! 
# 객체라고 생각하자! 

# 언제 사용할까? 
# list의 모든 원소가 어떤 정보가 필요할 떄 => key로 설정 
# 빠른 검색이 필요할 때! 

# 해쉬 장점 : 값을 찾는데 엄청 빠르다. (O(1))

from collections import Counter
print(Counter([1,2,3,4,3,3,2,2,1,2,3,2,1]).most_common(n = 2)) # 가장 많이 나온 2개! 
# most_common(n) : 가장 많이 나타난 n개! 
# 와.... 바로 나타나네! 
# 가장 많이 나온 수 

# N마리 포켓몬 중 N / 2마리를 가져가도 좋다 => N은 짝수이다. 
# ❗️포켓몬은 종류에 따라 번호를 붙여 구분한다❗️
# 최대한 많은 포켓몬 수!! 
# 즉, 종류 별로 한다음 종류의 수 만큼 선택한다! 

# 만약 골라야 하는 포켓몬 수! 

nums = [3,1,2,3]
poketmon_dic = Counter(nums)
print()
can_pick = len(nums) // 2
print(len(list(poketmon_dic))) # Counter객체를 바로 list로 바꾸면 공통 key들을 제거한 key값을 return받는다..! 

if len(list(poketmon_dic)) < can_pick:
    print(len(list(poketmon_dic)))
else:
    print(can_pick)