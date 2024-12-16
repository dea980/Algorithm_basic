def solution(numbers):
    numbers.sort()
    a = numbers[-1] 
    b = numbers[-2]
    answer= a*b
    return answer