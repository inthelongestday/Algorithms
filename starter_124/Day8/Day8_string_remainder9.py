# 문제 설명
# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
# 이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.

# 제한사항
# * 1 ≤ number의 길이 ≤ 100,000
# * number의 원소는 숫자로만 이루어져 있습니다.
# * number는 정수 0이 아니라면 숫자 '0'으로 시작하지 않습니다.

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
