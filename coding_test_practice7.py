#2016년
import datetime

def solution(a, b):
    answer = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return answer[datetime.datetime(2016,a,b).weekday()]




print(solution(5,24))
