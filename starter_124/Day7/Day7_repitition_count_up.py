# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# * 0 ≤ start_num ≤ end_num ≤ 50

def solution(start_num, end_num):
    answer = [x for x in range(start_num, end_num+1)]
    return answer

# 풀이 팁

# 1) range 함수 사용법 : list(range(start_num, end_num+1))
# 2) 같은 원리로 list 구성 : [x for x in range(start_num, end_num+1)]

# 두 방법 모두 range를 통해서 수를 나열하는 걸 활용해 list로 변환한 것!
