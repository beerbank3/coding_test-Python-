#가운데 글자 가져오기
#단어의 길이가 짝수라면 가운데 두글자 반환
def solution(s):
    if len(s)%2 == 0:
        answer = s[int(len(str2)/2-1):int(len(str2)/2+1)]
    else:
        answer = s[int(len(str2)/2):int(len(str2)/2+1)]
    return answer

str ="abcde"

str2 = "qwer"

print(solution(str2))