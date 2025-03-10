# 문제 설명
# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

# * "w" : n이 1 커집니다.
# * "s" : n이 1 작아집니다.
# * "d" : n이 10 커집니다.
# * "a" : n이 10 작아집니다.

# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# * -100,000 ≤ n ≤ 100,000
# * 1 ≤ control의 길이 ≤ 100,000
#   - control은 알파벳 소문자 "w", "a", "s", "d"로 이루어진 문자열입니다.

def solution(n, control):
    # case 'w'
    n += 1 * control.count('w')
    # case 's'
    n -= 1 * control.count('s')
    # case 'd'
    n += 10 * control.count('d')
    # case 'a'
    n -= 10 * control.count('a')
    return n

# 또 다른 풀이
# 각 문자에 따른 증감폭을 dictionary로 대응하여 대입

def solution(n, control):
    add = {'w':1, 's':-1, 'd':10, 'a':-10}
    for key in control:
        n += add[key]
    return n

# 근데 이게 속도는 좀 더 느린 것 같다..
