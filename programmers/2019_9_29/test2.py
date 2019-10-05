# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
#
# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.
# 입출력 예
# N	number	return
# 5	12	4
# 2	11	3
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.
#
# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

def solution(N, number):
    S = [[N]]
    print(S)
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, i // 2):
            print(X_i)
            print('for x in {}'.format(S[X_i]))
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        lst = list(set(lst))
        if number in lst:
            # print(S)
            return i
        S.append(lst)
    return -1


n_list = [5, 2, 5, 5, 5, 5]
number_list = [12, 11, 31168, 25, 23, 27]
return_list = [4, 3, -1, 2, 5, 5]


for i in range(len(n_list)):
    if solution(n_list[i], number_list[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))
