# 문제 설명

# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
# my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
# my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를
# 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * 1 ≤ my_string의 길이 ≤ 1,000

# String도 Iterable이다!!
# string에서 char을 하나하나 뽑을 때돋
# 그냥 for 문으로 for char in string: 이 가능하다는 걸 잊지 말자

def solution(my_string):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return [my_string.count(alph) for alph in alphabets.upper()+alphabets]
