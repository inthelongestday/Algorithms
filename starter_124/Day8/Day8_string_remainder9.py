# 문제 설명
# 

# 제한사항
# * 

def solution(number):
    num_sum = sum([int(num) for num in number.split()])
    return num_sum % 9

# 또 다른 풀이

# 이 경우 list를 새로 만드는 메모리가 들기 때문에
# 그냥 int answer 에다가 더하도록 만들어보자!

def solution(number):
    answer = 0
    for num in number:
        answer += int(num)
    return answer % 9

# 계산 속도도 단순 연산이 더 빠르다!
# 위에는 for 문 반복과 sum을 중복으로 하니까!!
