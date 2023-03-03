# chr(65) : 숫자를 문자로 바꿔주는 형변환인데 이걸 아스키로 사용함 
# ord("a") : 문자를 숫자로 바꿔준다..! 

char = input()

def printAscii(char):
    answer = ord(char)
    return answer

print(printAscii(char))