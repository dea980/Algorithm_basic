def solution(n, k):
    # 1 이상 n 이하의 수 중에서 k의 배수만 필터링하여 리스트로 반환
    answer = [i for i in range(1, n + 1) if i % k == 0]
    return answer
