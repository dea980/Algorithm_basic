import math
def solution(slice, n):
    answer = math.ceil(n/slice)
    # option 1
    # answer = ((n-1)//slice)+1
    # optin 2
    # d, m = divmod(n, slice)
    # return d + int(m != 0)
    return answer