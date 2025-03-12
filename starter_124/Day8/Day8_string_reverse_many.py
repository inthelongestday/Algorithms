# 문제 설명
# 

# 제한사항
# * 

def solution(my_string, queries):
    answer = ''
    for s, e in queries:
        my_substring = my_string[s:e+1]
        my_string = my_string[:s] + my_substring[::-1] + my_string[e+1:]
    return my_string

# 풀이 팁
# string indexing
# * [::a]는 a 간격씩 원소를 가져온다는 것인데,
#   [::-1]로 하면 -1, 즉 거꾸로 가져온다는 것이다.
#   [5::-1] 로 하면 index 5부터 거꾸로 원소를 가져올 것이다.
