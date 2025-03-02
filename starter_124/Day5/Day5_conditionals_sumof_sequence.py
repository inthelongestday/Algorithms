# 문제 설명
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * 1 ≤ a ≤ 100
# * 1 ≤ d ≤ 100
# * 1 ≤ included의 길이 ≤ 100
# * included에는 true가 적어도 하나 존재합니다.

def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        if included[i]:
            answer += a + i*d
    
    return answer

# 또 다른 / 더 나은 풀이

# 이게 만약 numpy 등을 import할 수 있는 상황이었다면
# 그냥 list masking을 통해서 바로 해결할 수 있는 문제였을 것이다.

import numpy as np

a = 3
d = 2

included = [False, True, True, False, True]

def solution(a, d, included):
    sequence = np.arange(a, a+((len(included))*d), d)
    trues = sequence[included]
    # print(sequence)
    # print(trues)
    # print(trues.sum())
    return trues.sum()

print(solution(a, d, included))
