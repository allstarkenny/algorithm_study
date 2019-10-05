# 문제 설명
# 가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다.
# 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다.
# 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.
#
# 타일을 가로로 배치 하는 경우
# 타일을 세로로 배치 하는 경우
# 예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.
#
# 직사각형의 가로의 길이 n이 매개변수로 주어질 때,
# 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.
#
# 제한사항
# 가로의 길이 n은 60,000이하의 자연수 입니다.
# 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.
# 입출력 예
# n	result
# 4	5

# 1 1 |                                        1
# 2 2 || =                                     1 + 1
# 3 3 ||| |= =|                                1 +
# 4 5 |||| ||= |=| =|| ==                      1 + 3 (3*2/2*1) = 3C2 + 1
# 5 8 ||||| |||= ||=| |=|| =||| ==| =|= |==    1 + 4 (4*3*2/3*2*1) = 4C3 + 3(3*2/2*1) = 3C2
# 6 13 |||||| ||||= |||=| ||=|| |=||| =|||| ==|| =|=| |==| =||= |=|= ||== ===     1 + 5(5*4*3*2/4*3*2*1) + 6(4*3/2*1) + 1

import math

def solution(n):
    return fibonacci(n+1)

def fibonacci(num):
    answer = [0, 1]
    for i in range(2, num + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1000000007)
    print(answer)
    return answer[-1]

def solution2(n):
    answer = 0
    items = [i for i in range(1, n+1)]
    for i in range(n):
        answer += cal_combination(items, i)
        items.pop()
        if len(items) <= 2:
            break
    answer += (n+1) % 2
    return answer

def cal_combination(a, b):
    # print(a[b:])
    # print(a[:len(a)-b])
    return cal_mul(a[b:]) // cal_mul(a[:len(a)-b])

def cal_mul(a):
    result = 1
    for i in a:
        result *= i
    return result

arr1 = [4, 5]
return_list = [5, 8]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))