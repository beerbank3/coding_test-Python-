#문자열 내 p와 y의 개수
#대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
#'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False
def solution(s):
    p_count = 0
    y_count = 0
    for i in range(len(s)):
        for i in s:
            if i == "p":
                p_count += 1
            elif i == "y":
                y_count += 1 
    return p_count == y_count

str = "pPoooyY"
print(solution(str))