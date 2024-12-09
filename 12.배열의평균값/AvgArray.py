
#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    sum = 0
    length = len(numbers)
    answer = 0
    #edge case 
    if length == 0:
        answer= 0
    for i in numbers:
        sum += i
    answer = sum/length
    
    return answer


## wrong answer
# def solution(numbers):
#     sum = 0
#     length = len(numbers)
#     answer = 0
#     for i in range numbers:
#         sum += i
#     answer = sum/length
#     return answer
## it gives the error TypeError: 'list' object cannot be interpreted as an intege
## it is beasue number is lists => so for that get rid of range
