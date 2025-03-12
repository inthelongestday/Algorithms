# 문제 설명
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * 1 ≤ my_string의 길이 ≤ 100
# * 1 ≤ is_suffix의 길이 ≤ 100
# * my_string과 is_suffix는 영소문자로만 이루어져 있습니다.


def solution(my_string, is_suffix):
    rev_str = my_string[::-1]
    rev_suffix = is_suffix[::-1]
    if rev_str.find(rev_suffix) == 0:
        return 1
    return 0

# 또 다른 풀이
# string.endswith(str) 활용

# 풀이 팁 : boolean은 그냥 자동 int로 인식되지 않는다.
# boolean을 꼭 return 값에 따라 int로 바꾸든 해서 return 하도록 하자.

def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

# 또 다른 풀이
# string 길이와 index 활용

def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)
