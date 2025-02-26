# 문제 설명
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 제한사항
# * 1 ≤ str1, str2의 길이 ≤ 10

str1, str2 = input().strip().split(' ')
print(str1+str2)
# 이 풀이는 두 string을 합친 새로운 string을 출력하는 방식이다.
# 기존의 str1, str2 외에 합쳐진 새로운 string을 할당한다는 단점이 있다 (메모리 상).

# 또 다른 풀이

print(str1, str2, sep='')
# 이 구문은 print 함수 자체의 seperator을 None으로 설정하여
# 두 변수를 공백 없이 붙여 출력하도록 한 것이다.

# 또 다른 풀이

print(input().strip().replace(' ', ''))
# 이 풀이는 공백을 기준으로 나뉘어 들어오는 여러 string에서
# 이 공백을 아예 None으로 replace하여 input을 쪼개지 않고 이어붙여서 출력하는 방식이다.
# 합친 string은 물론 str1, str2라는 별도의 변수를 할당하지 않는다는 차이점이 있다.

# 또 다른 풀이

print(''.join([str1, str2]))
# 이 풀이는 DE 할 때 궁금했던 건데, 그때는 join이 +보다 비효율적이기 때문에
# join을 사용해 concatenate된 모든 string을 단순 +로 변환하는 작업을 했었다.
# 뭔가.. 이 둘의 차이가 궁금해서 이런 reference 도 찾아봤으니 읽어보면 좋을 것 같다.
# 근데 효율상 두 개 정도면 +, 그 이상이거나 delimiter 를 다른 걸로 사용하고 싶을 경우 join을 사용하면 좋을 것 같다.
# - reference : https://medium.com/@yvan.siyou/stop-using-string-concatenation-in-python-the-superior-efficiency-of-join-explained-eae77d6c1595