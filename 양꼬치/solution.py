def solution(n, k):
    lamb = 12000*n
    k = k - int(n/10)
    drink = 2000*k
    answer= lamb + drink
    return answer