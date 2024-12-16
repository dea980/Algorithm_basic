def solution(cipher, code):
    answer = [y for x, y in enumerate(cipher) if (x + 1) % code == 0]
    return ''.join(answer)