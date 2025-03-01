# 문제 설명
# 

# 제한사항
# * 

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