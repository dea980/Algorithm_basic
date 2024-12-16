def solution(a, b):

    c =str(a)+str(b)
    d = 2 * a * b
    if int(c) > d:
        return int(c)
    else:
        return d
