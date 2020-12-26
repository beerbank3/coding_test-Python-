#문자열 다루기 기본
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수
#s 가 a234 False
#s 가 1234aus True
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isalpha():
                return False
        return True
    else:
        return False

s ="12132"

print(solution(s))