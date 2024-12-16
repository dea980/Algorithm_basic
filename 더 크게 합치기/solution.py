def solution(a, b):
    m = str(a) + str(b)
    n = str(b) + str(a)
    if int(m) >= int(n):
        return int(m)
    else:
        return int(n)