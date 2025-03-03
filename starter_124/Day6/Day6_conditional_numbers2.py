# 문제 설명
# 정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

# * "w" : 수에 1을 더한다.
# * "s" : 수에 1을 뺀다.
# * "d" : 수에 10을 더한다.
# * "a" : 수에 10을 뺀다.

# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.
# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# * 2 ≤ numLog의 길이 ≤ 100,000
#   - -100,000 ≤ numLog[0] ≤ 100,000
#   - 1 ≤ i ≤ numLog의 길이인 모든 i에 대해 |numLog[i] - numLog[i - 1]|의 값은 1 또는 10입니다.

def solution(numLog):
    answer = ''
    map = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(1, len(numLog)):
        answer += map[numLog[i]-numLog[i-1]]
    return answer

# numbers1 에서 또 다른 풀이로 적은 방식을 차용했다.
# 시간은 좀 느린 편이다.
# numbers1 에서 본 풀이로 적었던 방식으로 풀면 어떻게 될까
# 메모리 사용을 감안하고, diff list로 변환하면 어떻게 될까

def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):
        diff = numLog[i]-numLog[i-1]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    return answer

# 속도는 조금 빠르지만 메모리 사용은 비슷하다
# 별 차이 없다고 봐도 될 듯! 좀 더 간단하냐의 논점에서 보면 위의 것이 낫겠지만
# 아래 것이 직관적이긴 할 것이다. (하지만 too naive..)
