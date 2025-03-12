# 문제 설명
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * my_string은 알파벳 소문자로만 이루어져 있습니다.
# * 1 ≤ my_string의 길이 ≤ 100

def solution(my_string):
    answer = sorted([my_string[-i:] for i in range(1, len(my_string)+1)])
    return answer

# list sorting
# list.sort() : list 자체를 sort하지만, return 값이 None이다.
# * 따라서 return list.sort()를 하면 null을 return한다.
# * 이때 그냥 a 를 return 하면 제대로 return 한다.

def solution(my_string):
    answer = [my_string[-i:] for i in range(1, len(my_string)+1)]
    answer.sort() # sort는 그냥 function으로 돌려주고 (return None)
    return answer # return은 그냥 sort된 answer을 하면 된다!

# 그에 비해 sorted는 정렬된 새로운 list를 반환한다.
