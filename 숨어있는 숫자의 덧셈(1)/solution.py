def solution(my_string):
    answer = 0
    for j in my_string:
        if j.isdigit():
            answer += int(j)
    return answer