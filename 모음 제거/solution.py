def solution(my_string):
    answer = ''
    vowel = 'a, e, i ,o ,u'
    for i in my_string:
        if i not in vowel or i == ' ': ## since it does not cover space..
            answer += i
    return answer
     # return ''.join([i for i in my_string if i not in vowel or i ==' '])
    #  vowels = ['a','e','i','o','u']
    # for i in vowels:
    #     my_string = my_string.replace(i, '')
    # return my_string