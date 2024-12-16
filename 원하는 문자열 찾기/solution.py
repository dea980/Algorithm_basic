def solution(myString, pat):
    answer = 0
    m = myString.lower()
    n = pat.lower()
    if n in m:
        answer += 1
    else:
        answer == 0
    return answer