# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
#
# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

def solution(n, m):
    answer = []
    # 최대공약수 계산
    s, l = (min([n,m]), max([n,m]))

    answer.append(calmod(s, l))
    answer.append(answer[0] * (n // answer[0]) * (m // answer[0]))

    return answer

def calmod(a, b):
    if a % b == 0:
        return b
    else:
        return calmod(b, a % b)


# c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]
#
#     return answer

arr_1 = [3, 2]
arr_2 = [12, 5]
return_list = [[3, 12], [1, 10]]

for i in range(len(arr_1)):
    if solution(arr_1[i], arr_2[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 17 min