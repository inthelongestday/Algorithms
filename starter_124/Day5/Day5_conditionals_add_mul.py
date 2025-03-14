# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# * 2 ≤ num_list의 길이 ≤ 10
# * 1 ≤ num_list의 원소 ≤ 9

def solution(num_list):
    res_mul = 1
    for num in num_list:
        if num == 0:
            res_mul = 0
            break
        res_mul *= num
    res_sum = sum(num_list)**2
    return int(res_mul < res_sum)
