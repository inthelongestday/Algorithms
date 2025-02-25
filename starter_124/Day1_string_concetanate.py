# 문제 설명
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 제한사항
# * 1 ≤ str의 길이 ≤ 10
# * 1 ≤ n ≤ 5

str, n = input().strip().split(' ')
n = int(n)

# 나의 풀이
# newstr = ''
# for i in range(n):
#     newstr += str
# print(newstr)

# 더 좋은 풀이
print (str * int(n))
# * n이 string으로 들어오기 때문에 int로 변환
# * string에 정수를 곱하면 그 횟수만큼 반복된 string이 생성된다