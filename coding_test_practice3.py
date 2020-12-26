#완주하지 못한 선수
import collections
def solution(participant, completion):
    participant.sort()
    completion.sort()
    result = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    return list(result)[0]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(collections.Counter(participant))