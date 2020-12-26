#모의고사
from itertools import cycle
def solution(answers):
    win = []
    answer_temp = []
    count = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for ans1, ans2, ans3,answer in zip(cycle(a), cycle(b), cycle(c), answers):
        if ans1 == answer:
            count[0]+=1
        if ans2 == answer:
            count[1]+=1
        if ans3 == answer:
            count[2]+=1

    for person, score in enumerate(count):
        if score == max(count):
            win.append(person+1)
    return win

answers = [1,2,3,4,5]
print(solution(answers))