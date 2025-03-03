# 문제 설명
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

# 제한사항
# * 1 ≤ arr의 길이 ≤ 1,000
#   - 0 ≤ arr의 원소 ≤ 1,000,000
#   - 1 ≤ queries의 길이 ≤ 1,000
# * 0 ≤ s ≤ e < arr의 길이
#   - 0 ≤ k ≤ 1,000,000

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        in_range = [x for x in arr[s:e+1] if x > k]
        if len(in_range):
            answer.append(min(in_range))
        else:
            answer.append(-1)
    return answer

# list 내에서 특정 조건 만족하는 원소만 남기는 법 (masking):
# numpy 처럼 masking이 안될 경우에는,
# (numpy의 경우에는 그냥 arr[arr > 3] 뭐 이런식으로 boolean masking 하면 됨)
# for문으로 iteration하는 끝에 조건문 붙이면 됨!!
# 그럼 위처럼 조건에 맞는 원소만 거를 수 있다!

# 그리고 list 같은 iterable은 min, max로 최대최소 구할 수 있음
