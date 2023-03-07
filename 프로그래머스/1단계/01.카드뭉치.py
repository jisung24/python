# cards1	cards2	goal	result
# ["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"
# ["i", "water", "drink"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"No"

goal = ["i", "want", "to", "drink", "water"]
cards1  = ["i", "drink", "water"]
cards2 = ["want", "to"]

def solution(cards1, cards2, goal):
    for i in goal:
        print(i)
        if cards1[0] == i:
            # 0번째에 반드시 있어야 돼! 
            cards1.pop(0)
            print(f"남아있는 cards1 >> {cards1}")
        elif cards2[0] == i:
            cards2.pop(0)
            print(f"남아있는 cards2 >> {cards1}")
        else:
            return "No"
        
    if len(cards1) == 0 and len(cards2) == 0:
        return "Yes"
    
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))


arr = [1,2,3,4,5]
print(arr.pop(0))
print(arr[0])
print(arr[0])
print(arr[0])
print(arr[0])
print(arr[0])