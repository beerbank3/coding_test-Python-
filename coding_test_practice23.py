#약수의 합
#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수
def solution(n):
    answer = 0
    for i in range(1,int(n/2+1)):
        if n%i == 0:
            answer += i
            if(int(n/i)>int(n/2)):
                answer += int(n/i)
    return answer


n = 1
print(solution(n))