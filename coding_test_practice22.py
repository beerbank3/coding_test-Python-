#시저 암호
#예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
#chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
#ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다. 
def solution(s, n):
    answer =''
    for i in s:
        if i.isupper():
            answer += chr((ord(i)-ord('A')+n)%26+ord('A'))
        elif i.islower():
            answer += chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer += i
    return answer


s = "AB"
n  = 1
print(solution(s,n))