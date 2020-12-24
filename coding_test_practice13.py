#문자열 내 마음대로 정렬하기

#문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때
#각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
#strings가 [sun, bed, car]이고
#n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬
#https://docs.python.org/3/howto/sorting.html lambda 문서
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])

strings = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings2,n))