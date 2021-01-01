#이상한 문자 만들기
#각 단어는 하나 이상의 공백문자로 구분
#각 단어의 짝수번째 알파벳은 대문자로
#홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수
def solution(s):
    answer = ''
    index = True
    for i in s:
        if i.isspace():
            answer += i
            index = True
        else:
            if index:
                answer += i.upper()
                index = False
            else:
                answer += i.lower()
                index = True
    return answer


s = "try dsad ewc asdf world"

print(solution(s))