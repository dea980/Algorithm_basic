def solution(n, t):
    # return n<<t bit 연산
    if t == 0:  # 종료 조건: t가 0이 되면 더 이상 재귀하지 않음
        return n
    return solution(2 * n, t - 1)  # n을 두 배로 하고, t를 1 줄임