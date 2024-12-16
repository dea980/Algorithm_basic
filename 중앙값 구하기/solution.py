def solution(array):
    array.sort()
    middle = len(array)//2
    answer = array[middle]
    return answer