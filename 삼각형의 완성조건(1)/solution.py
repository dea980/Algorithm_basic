import math 
def solution(sides):
    answer = 0
    # longest = math.max(slides)
    sides.sort()
    summation = sides[0] +sides[1]
    if summation > sides[2]:
        answer +=1
    else:
        answer +=2
    
    return answer

#  1 if max(sides) < (sum(sides) - max(sides)) else 2
