# 문제 설명
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다.
# queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
# my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * my_string은 영소문자로만 이루어져 있습니다.
# * 1 ≤ my_string의 길이 ≤ 1,000
# * queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
# * 1 ≤ queries의 길이 ≤ 1,000

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
