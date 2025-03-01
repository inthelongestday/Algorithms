# 문제 설명
# 

# 제한사항
# * 

def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return 1 if n <= m else 0
        else:
            return 1 if n < m else 0
    else:
        if eq == "=":
            return 1 if n >= m else 0
        else:
            return 1 if n > m else 0
        
# 또 다른 풀이
# conditional 구문은 그 값이 true일 경우 1, false일 경우 0인 점을 활용하여
# ' return 1 if (condition) else 0 ' 의 구문 대신
# ' int(condition) ' 으로 return값을 조정할 수 있다
# 또한, input이 잘못 들어오는 경우 -> 즉 예외처리를 해주면 더 좋은 답안이 될 수 있다!

def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        else:
            return int(n < m)
    else:
        if eq == "=":
            return int(n >= m)
        else:
            return int(n > m)

# 또한 이 경우 외에도, 조건을 나처럼 nested로 하지 않고
# 개별 경우로 모두 분류한 후, 문자열 조건과 실제 수학 조건을 동시에 만족하는 경우에 1을 return,
# 그 외 경우에는 default 값인 0을 return하도록 하여 예외처리를 하는 답안도 좋은 것 같다.