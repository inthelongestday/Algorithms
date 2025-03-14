# 문제 설명
# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다.
# 정수 idx가 주어졌을 때, idx보다 크거나 같으면서
# 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
# 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

# 제한사항
# * 3 ≤ arr의 길이 ≤ 100'000
#   - arr의 원소는 전부 1 또는 0입니다.

def solution(arr, idx):
    if 1 not in arr[idx:]:
        return -1
    else:
        return idx+arr[idx:].index(1)

# slicing한 list의 index는
# 원래 list의 index와 다르다는 걸 잊지 말자...

# list = [1, 2, 3, 4, 5]

# list.find(5) >> 4
# list[3:].find(5) >> 2    원소 5 의 위치가 달라질 수밖에 없다..

# - list[3:] = [3, 4, 5]
