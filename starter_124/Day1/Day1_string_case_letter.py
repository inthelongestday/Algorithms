# 문제 설명
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다.
# 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 제한사항
# * 1 ≤ str의 길이 ≤ 20
#   - str은 알파벳으로 이루어진 문자열입니다.

# 풀이 팁
# 이 문제는 python의 string 메소드 중 "swapcase()" 를 사용하는 문제이다.
# Reference URL
# * https://www.geeksforgeeks.org/python-string-methods/?ref=lbp
# * https://www.geeksforgeeks.org/python-string-swapcase/

str = input()
print(str.swapcase())
