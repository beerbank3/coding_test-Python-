#두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in numbers:
        if numbers.count(i) > 1:
            answer.append(i+i)
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2:
                answer.append(num1+num2)
    answer = list(set(answer))
    return answer

numbers = [2,1,3,4,1]

print(solution(numbers))