def solution(num_list):
    answer = 0
    summation = 0
    multi = 1
    for num in num_list:
        summation += num
        multi *= num
    #print(summation, multi)
    if summation**2 > multi:
        answer +=1
    else:
        answer = 0
    return answer