# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지
#  1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# * 0 ≤ end_num ≤ start_num ≤ 50

# 원래 순서대로 원소를 받아서 [::-1] 로 거꾸로 받기
def solution(start_num, end_num):
    answer = list(range(end_num, start_num+1))[::-1]
    return answer

# 또 다른 풀이
# 처음부터 -1 간격으로 거꾸로 받기
def solution(start_num, end_num):
    answer = list(range(start_num, end_num-1, -1))
    return answer
