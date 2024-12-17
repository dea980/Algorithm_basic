def solution(myString):
    result = []
    for char in myString:
        if char == 'a':
            result.append('A')  # 'a'를 'A'로 변환
        elif 'A' <= char <= 'Z' and char != 'A':
            result.append(char.lower())  # 'A'가 아닌 대문자를 소문자로 변환
        else:
            result.append(char)  # 나머지는 그대로
    return ''.join(result)
