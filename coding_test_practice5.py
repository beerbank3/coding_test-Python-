#체육복
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 체육수업을 들을 수 있는 학생의 최댓값을 return
def solution(n, lost, reserve):
    lostA = set(lost) - set(reserve)
    reserveA = set(reserve) - set(lost)

    n -= len(lostA)
    for i in lostA:
        for j in reserveA:
            if j == (i-1) or j == (i+1):
                n += 1
                reserveA.remove(j)
                break
    return n

n = 20
lost = [8,11,12]
reserve = [1,3,14,16,17,18,19,20]

print(solution(n,lost,reserve))