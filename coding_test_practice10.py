#같은 숫자는 싫어
def solution(arr):
    answer = []
    for i in arr:
        if len(answer)>0 and i == answer[-1]:
            pass
        else:
            answer.append(i)
    return answer

arr = [1,1,3,3,0,1,1]

print(solution(arr))