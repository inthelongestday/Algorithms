# 문제 설명
# 정수 리스트 num_list가 주어질 때,
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을,
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을,
# 추가하여 return하도록 solution 함수를 완성해주세요.

# 제한사항
# * 2 ≤ num_list의 길이 ≤ 10
# * 1 ≤ num_list의 원소 ≤ 9

def solution(num_list):
    num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1]*2)
    return num_list

# 풀이 팁
# * list의 마지막 원소를 indexing할 때는 -1부터 역으로 센다
#   - list[-1] : 마지막 원소
#   - list[-2] : 마지막에서 두 번째 원소
#   - ...
# * list에 원소를 추가하는 method는 append이다.
# * list 관련 method에 대해 읽어보자
#   - reference : https://wikidocs.net/14
