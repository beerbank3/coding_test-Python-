#소수 찾기
#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수
def solution(n):
    num = [True] * (n+1)
    for i in range(2, int(n ** 0.5)+1):
        if num[i]:
            for j in range(i+i,n+1,i):
                num[j] = False

    return len([i for i in range(2,(n+1)) if num[i]])
n = 10

print(solution(n))


def solution2(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

print(solution2(n))