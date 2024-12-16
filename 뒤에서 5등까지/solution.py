def solution(num_list):
    sorted_list = sorted(num_list)
    ## 아마 에러 여기서 날듯 answer.append(sorted_list[1:5])
    ## 굳이...? answer?을? 다시 넣을 필요가 있는가?
    ## Therefore,  ##
    answer= sorted_list[0:5]
    
    print(num_list.sort()) ## 왜 None 이 나오나?
    return answer
    