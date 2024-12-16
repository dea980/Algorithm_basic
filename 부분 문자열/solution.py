def solution(str1, str2):
    # answer = 0
    # if str1 in str2:
    #     answer +=1
    # else:
    #     answer = 0
    # return answer
    answer = 0
    len1 = len(str1)
    len2 = len(str2)
    
    # str1의 길이가 str2보다 길면 부분 문자열이 될 수 없음
    if len1 > len2:
        return 0
    
    # str2를 순회하며 str1과 비교
    for i in range(len2 - len1 + 1):
        if str2[i:i+len1] == str1:
            return 1  # 부분 문자열 발견 시 바로 리턴
    
    return 0  # 발견되지 않으면 0 리턴