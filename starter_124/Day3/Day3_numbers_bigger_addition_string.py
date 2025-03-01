# 문제 설명
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# - 12 ⊕ 3 = 123
# - 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

# 제한사항
# * 1 ≤ a, b < 10,000

def solution(a, b):
    len_a = len(str(a))
    len_b = len(str(b))
    
    answer_a = a * (10**len_b) + b
    answer_b = b * (10**len_a) + a
        
    return answer_a if answer_a >= answer_b else answer_b

# 더 나은 풀이
# str 상태에서 값을 합친 후 비교하자!
# 이때 string concatenation은 + 혹은 f string으로도 가능하다.

def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    
    return max(int(str_a+str_b), int(str_b+str_a))

# 놀라운 사실 : 이 풀이가 더 간단해 보여도, 내 풀이보다 속도가 더 느리다!
# max나 int 계산이 나의 단순 연산자보다 느린가보다.