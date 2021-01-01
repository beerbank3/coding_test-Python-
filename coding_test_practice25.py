#자릿수 더하기
#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return
def solution(n):
    answer = 0
    while True:
        answer += n%10
        n = int(n/10)
        if n < 10:
            answer += n
            break
    return answer


n = 1234
print(solution(n))