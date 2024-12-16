def solution(num_list):
    even = 0
    odd = 0
    for x in num_list:
        if x % 2 == 1:
            odd +=1
        else:
            even +=1
    answer = [even, odd]
    return answer