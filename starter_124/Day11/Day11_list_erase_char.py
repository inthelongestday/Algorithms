# 문제 설명

# 문자열 my_string과 정수 배열 indices가 주어질 때, 
# my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을
# return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * 1 ≤ indices의 길이 < my_string의 길이 ≤ 100
# * my_string은 영소문자로만 이루어져 있습니다
# * 0 ≤ indices의 원소 < my_string의 길이
# * indices의 원소는 모두 서로 다릅니다.

def solution(my_string, indices):
    list = [my_string[i] for i in range(len(my_string)) if i not in indices]
    return ''.join(list)

# list 내부에서 iterable enumerate할 때 조건 거는 법
# 까먹지 말기!!

# 또, 접근방법으로
# string은 불변이다. (immutable)
# 그에 비해 list는 가변이기 때문에 (mutable)
# string 내부의 일부 원소를 바꾸거나 삭제해서 다시 붙이는
# 그런 종류의 문제의 경우,
# string을 list화해서 접근하도록 한다.
# 그 방법은 아래와 같다.

# * list(str) : str 을 char 하나씩 list화 함
# * str.split() : 공백을 default로 하는 delimiter 기준으로 str를 쪼개 list를 반환.

# string : iterable, immutable
# list : itreable, mutable

# 둘 다 iterable이기 때문에 바로 string[i] indexing이 가능하다는 것도 잊지 말 것!
# 다만 append, pop, del, remove같은 수정이 안되는 것뿐!!
