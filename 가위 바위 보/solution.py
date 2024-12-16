def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':  # '가위'의 경우
            answer += '0'
        elif i == '0':  # '바위'의 경우
            answer += '5'
        elif i == '5':  # '보'의 경우
            answer += '2'
    return answer