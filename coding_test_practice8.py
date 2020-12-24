#3진법 뒤집기
def solution(n):
    num = 0
    answer = []
    for i in range(20, -1, -1):
        if int(n/(3**i)>=1):
            answer.append(int(n/(3**i)))
            n = n %(3**i)
        elif len(answer) > 0 and int(n/(3**i)<1):
            answer.append(0)
    print(answer)
    for i in range(0,len(answer)):
        if answer[i] > 0:
            num += answer[i] * (3**i)
    return num

n = 845621545

print(solution(n))