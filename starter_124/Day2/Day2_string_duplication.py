# 문제 설명
# 

# 제한사항
# * 

def solution(my_string, overwrite_string, s):
    string_list = list(my_string)
    string_list[s:s+len(overwrite_string)] = list(overwrite_string)
    answer = ''.join(string_list)
    return answer

# 더 좋은 풀이
# 굳이 list로 변환할 필요가 없었다. 그냥 잘라붙이면 되지..
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]