def solution(num_list):
    odd = ''.join(str(i) for i in num_list if i%2 != 0)
    even =''.join(str(j) for j in num_list if j%2 == 0)
    answer = int(odd)+ int(even)
    return answer