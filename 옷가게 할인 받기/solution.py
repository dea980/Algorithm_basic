def solution(price): ## 정수 문제여서 int 필요
    if 100000 <= price < 300000:
        return int(price * 0.95)
    elif 300000 <= price < 500000:
        return int(price * 0.9)
    elif price >= 500000:
        return int(price * 0.8)
    else:
        return price