# 문제 설명
# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서
# k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# * 1 ≤ n ≤ 1,000,000
# * 1 ≤ k ≤ min(1,000, n)

def solution(n, k):
    answer = list(range(k, n+1, k))
    return answer

# 몫과 나머지, mod, 배수/공배수 등은 결국 등차수열,
# 즉, 간격을 활용하는 풀이를 요구한다는 걸 잊지 말자!
# * range(시작, 끝, 간격)
# * string[시작:끝:간격]
