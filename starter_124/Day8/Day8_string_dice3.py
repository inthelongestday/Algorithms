# 문제 설명
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# * 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# * 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# * 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# * 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# * 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# * a, b, c, d는 1 이상 6 이하의 정수입니다.


def solution(a, b, c, d):
    numlist = [a, b, c, d]
    cntlist = [numlist.count(x) for x in numlist]
    print(cntlist)
    
    if max(cntlist) == 4:
        return 1111*numlist[cntlist.index(4)]
    elif max(cntlist) == 3:
        return (10*numlist[cntlist.index(3)]+numlist[cntlist.index(1)])**2
    elif max(cntlist) == 2:
        if cntlist.count(2) == 4:
            p = list(set(numlist))[0]
            q = list(set(numlist))[1]
            return (p+q)*abs(p-q)
        else:
            qidx = cntlist.index(1)
            ridx = cntlist.index(1, qidx+1)
            # 리스트 index 함수
            # index (찾고 싶은 값, 범위 앞, 범위 끝)
            q = numlist[qidx]
            r = numlist[ridx]
            return q*r
    else:
        return min(numlist)
