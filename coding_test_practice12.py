#두 정수 사이의 합
#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한
#모든 정수의 합을 리턴하는 함수
def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer += i
    else:
        for i in range(a,b-1,-1):
            answer += i
    return answer


a = 5
b = 3

print(solution(a,b))