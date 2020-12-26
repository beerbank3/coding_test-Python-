#수박수박수박수박수박수?
#n이 4이면 수박수박을 리턴하고 3이라면 수박수 리턴
from itertools import cycle
def solution(n):
    answer = ''
    str1 = "수박"
    for i,j in zip(cycle(str1),range(n)):
            answer += i
    return answer

n = 5
print(solution(n))