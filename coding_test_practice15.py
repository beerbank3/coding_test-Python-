#문자열 내림차순으로 배치하기
def solution(s):
    answer = ""
    big = []
    small = []
    for i in s:
        if i.isupper():
            big.append(i)
        else:
            small.append(i)
    small.sort()
    big.sort()
    small.reverse()
    big.reverse()
    for i in small:
        answer += i
    for i in big:
        answer += i
    return answer

s = "ZbcdeAafg"

print(solution(s))
#print(sorted(s))

def solution2(s):
    return ''.join(sorted(s, reverse=True))

print(solution2(s))
