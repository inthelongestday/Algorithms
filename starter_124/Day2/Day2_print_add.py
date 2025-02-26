# 문제 설명
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
# a + b = c

# 제한사항
# * 1 ≤ a, b ≤ 100

a, b = map(int, input().strip().split(' '))
print(a, "+", b, "=", a + b)

# input() 은 사용자 입력을 받는 함수이다.
# strip() 은 string 앞뒤의 특정 문자를 제거하는 함수이다. default는 공백 문자이다.
# - reference : https://docs.python.org/ko/3.13/library/stdtypes.html#str.split
# split() 은 string 을 특정 문자 기준으로 쪼개는 함수이다. default는 공백 문자이다.
# - output 형태는 리스트이다. 리스트를 string 여러 개로 받을 수 있다.
# - reference : https://docs.python.org/ko/3.13/library/stdtypes.html#str.split
