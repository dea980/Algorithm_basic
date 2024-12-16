def solution(n):
    
    # odd
    if n%2 ==1:
        return sum(i for i in range(1, n+1, 2)) ## 홀수의 합
    # even
    if n%2 ==0: ### sum of power
        return sum(j**2 for j in range(2,n+1, 2))