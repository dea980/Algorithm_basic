def solution(n):
    count = 0  # 순서쌍의 개수
    for a in range(1, int(n ** 0.5) + 1):  # 1부터 √n까지 반복
        if n % a == 0:  # a가 n의 약수라면
            b = n // a
            count += 1  # (a, b) 추가
            if a != b:  # a와 b가 같지 않다면 (b, a)도 추가
                count += 1
    return count
