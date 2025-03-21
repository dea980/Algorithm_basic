##x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
# x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
# x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
# x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

def solution(dot):
    if dot[0] > 0 and dot[1] > 0:  # First quadrant
        return 1
    elif dot[0] > 0 and dot[1] < 0:  # Fourth quadrant
        return 4
    elif dot[0] < 0 and dot[1] < 0:  # Third quadrant
        return 3
    elif dot[0] < 0 and dot[1] > 0:  # Second quadrant
        return 2
