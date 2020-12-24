#나누어 떨어지는 숫자 배열
#array의 각 element 중 divisor로 나누어 떨어지는 값을
# 오름차순으로 정렬한 배열을 반환하는 함수
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer


arr = [3,2,6]
divisor = 10

print(solution(arr,divisor))