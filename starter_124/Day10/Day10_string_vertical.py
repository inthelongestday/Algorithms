# 문제 설명
# 문자열 my_string과 두 정수 m, c가 주어집니다.
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로
# c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * my_string은 영소문자로 이루어져 있습니다.
# * 1 ≤ m ≤ my_string의 길이 ≤ 1,000
# * m은 my_string 길이의 약수로만 주어집니다.
# * 1 ≤ c ≤ m

def solution(my_string, m, c):
    sh = len(my_string) // m
    r = len(my_string) % m
    if r < c:
        return ''.join([my_string[(c-1)+m*i] for i in range(sh)])
    else:
        return ''.join([my_string[(c-1)+m*i] for i in range(sh+1)])
    return answer

# 더 나은 풀이
# 애초에 list는 시작, 끝, 간격을 지정해서 원소를 return할 수가 있다.

def solution(my_string, m, c):
    return my_string[c-1::m]

# 이렇게 주기적 간격으로 원소를 반환할 경우,
# 간격으로 indexing 하는 걸 잊지 말자!
