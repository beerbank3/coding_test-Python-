#자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    while True:
        answer.append(n%10)
        n = int(n/10)
        if n < 10:
            answer.append(n)
            break
    return answer


n = 5
print(solution(n))