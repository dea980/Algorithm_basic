def solution(my_string, is_suffix):
    # Check if the length of `is_suffix` is less than or equal to `my_string`
    if len(is_suffix) <= len(my_string) and my_string[-len(is_suffix):] == is_suffix:
        return 1
    return 0
    # if my_string.endswith(is_suffix):
    #     return 1
    # return 0