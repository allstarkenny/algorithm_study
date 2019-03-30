# 문제 설명
# 숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. 게임해보기
#
# 각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다.
# 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.
#
# * 숫자는 맞지만, 위치가 틀렸을 때는 볼
# * 숫자와 위치가 모두 맞을 때는 스트라이크
# * 숫자와 위치가 모두 틀렸을 때는 아웃
# 예를 들어, 아래의 경우가 있으면
#
# A : 123
# B : 1스트라이크 1볼.
# A : 356
# B : 1스트라이크 0볼.
# A : 327
# B : 2스트라이크 0볼.
# A : 489
# B : 0스트라이크 1볼.
# 이때 가능한 답은 324와 328 두 가지입니다.
#
# 질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때,
# 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 질문의 수는 1 이상 100 이하의 자연수입니다.
# baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.


def solution(baseball):
    answer = 0
    test_search = []
    baseball.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print(baseball)
    number, strike, ball = baseball[0]
    if strike == 3:
        return 1
    baseball.remove(baseball[0])

    pattern = make_pattern(number, strike, ball)
    print(pattern)
    for number, strike, ball in baseball:

        pattern = check_pattern(pattern, number, strike, ball)
        print('#######################')

    print(pattern)

    return answer

def make_pattern(number, strike, ball):
    pattern = []
    print(str(number))
    a, b, c = str(number)
    other_numlist = ['1','2','3','4','5','6','7','8','9']
    other_numlist.remove(a)
    other_numlist.remove(b)
    other_numlist.remove(c)

    if strike == 0:
        if ball == 0:
            pattern.append([other_numlist, other_numlist, other_numlist])
        elif ball == 1:
            pattern.append([b, other_numlist, other_numlist])
            pattern.append([c, other_numlist, other_numlist])
            pattern.append([other_numlist, a, other_numlist])
            pattern.append([other_numlist, c, other_numlist])
            pattern.append([other_numlist, other_numlist, a])
            pattern.append([other_numlist, other_numlist, b])
        elif ball == 2:
            pattern.append([b, c, other_numlist])
            pattern.append([b, a, other_numlist])
            pattern.append([b, other_numlist, a])
            pattern.append([c, a, other_numlist])
            pattern.append([other_numlist, a, b])
            pattern.append([c, other_numlist, a])
            pattern.append([c, other_numlist, b])
            pattern.append([other_numlist, c, a])
            pattern.append([other_numlist, c, b])
        else:
            pattern.append([b, c, a])
            pattern.append([c, a, b])
    elif strike == 1:
        if ball == 0:
            pattern.append([a, other_numlist, other_numlist])
            pattern.append([other_numlist, b, other_numlist])
            pattern.append([other_numlist, other_numlist, c])
        elif ball == 1:
            pattern.append([a, c, other_numlist])
            pattern.append([a, other_numlist, b])
            pattern.append([c, b, other_numlist])
            pattern.append([other_numlist, b, a])
            pattern.append([b, other_numlist, c])
            pattern.append([other_numlist, a, c])
        else:
            pattern.append([a, c, b])
            pattern.append([c, b, a])
            pattern.append([b, a, c])
    elif strike == 2:
        pattern.append([a, b, other_numlist])
        pattern.append([a, other_numlist, c])
        pattern.append([other_numlist, b, c])

    # str 0 and ball 0 -> 0
    # [- - -]
    # str 0 and ball 1 -> 6
    # [b - -] [c - -] [- a -] [- c -] [- - a] [- - b]
    # str 0 and ball 2 -> 9
    # [b c -] [b a -] [b - a] [c a -] [- a b] [c - a] [c - b] [- c a] [- c b]
    # str 0 and ball 3 -> 2
    # [b c a] [c a b]
    # str 1 and ball 0 -> 3
    # [a - -] [- b -] [- - c]
    # strike 1 and ball 1 -> 6
    # [a c -] [a - b] [c b -] [- b a] [b - c] [- a c]
    # str 1 and ball 2 -> 3
    # [a c b] [c b a] [b a c]
    # str 2 and ball 0 -> 3
    # [a b -] [a - c] [- b c]
    return pattern


def check_pattern(pattern, number, strike, ball):
    print('{} insert pattern {} {}'.format(number, strike, ball))
    a, b, c = str(number)
    local_pattern = []
    for p1, p2, p3 in pattern:
        print([p1, p2, p3])
        # strike check
        strike_cnt = 0
        if check_strike(a, p1):
            strike_cnt += 1
        if check_strike(b, p2):
            strike_cnt += 1
        if check_strike(c, p3):
            strike_cnt += 1
        print('strike = {}'.format(strike_cnt))
        if strike_cnt != strike:
            continue

        # ball check
        ball_cnt = 0
        if check_strike(a, p2) or check_strike(a, p3):
            ball_cnt += 1
        if check_strike(b, p1) or check_strike(b, p3):
            ball_cnt += 1
        if check_strike(c, p1) or check_strike(c, p2):
            ball_cnt += 1
        print('ball = {}'.format(ball_cnt))
        # if ball_cnt != ball:
        #     continue
        # print([p1, p2, p3])
        local_pattern.append([make_param(a, b, c, p1),
                              make_param(a, b, c, p2),
                              make_param(a, b, c, p3)])

    return local_pattern


def check_strike(a, b):
    if isinstance(b, list):
        # if a in b:
        #     return True
        return False
    else:
        if a == b:
            return True
    return False

def make_param(a, b, c, param):
    if isinstance(param, list):
        if a in param:
            param.remove(a)
        if b in param:
            param.remove(b)
        if c in param:
            param.remove(c)
    return param

arr1 = [[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]]
return_list = [2]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))