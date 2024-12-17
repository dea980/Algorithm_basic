from functools import cmp_to_key

def solution(numbers):
    # 두 수를 이어 붙였을 때 비교하는 함수
    def compare(x, y):
        if x + y > y + x:
            return -1  # x가 앞에 와야 함
        elif x + y < y + x:
            return 1   # y가 앞에 와야 함
        else:
            return 0   # 같으면 그대로 유지

    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 정렬: 커스텀 비교 함수를 사용
    str_numbers.sort(key=cmp_to_key(compare))
    
    # 결과를 이어 붙이기
    result = ''.join(str_numbers)
    
    # 결과가 0으로 시작하면 0 반환
    return '0' if result[0] == '0' else result
