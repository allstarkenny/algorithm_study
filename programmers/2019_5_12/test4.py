# 문제 설명
# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
#
# 예를 들어, 문자열 S = baabaa 라면
#
# b aa baa → bb aa → aa →
#
# 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
#
# 제한사항
# 문자열의 길이 : 1,000,000이하의 자연수
# 문자열은 모두 소문자로 이루어져 있습니다.
# 입출력 예
# s	result
# baabaa	1
# cdcd	0
# 입출력 예 설명
# 입출력 예 #1
# 위의 예시와 같습니다.
# 입출력 예 #2
# 문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.

import itertools
def solution(s):
    before_len = len(s)
    while before_len > 0:
        s = ''.join(itertools_test(s))
        if before_len == len(s):
            return 0
        before_len = len(s)
    return 1

def itertools_test(s):
    return_data =[]
    for k, v in itertools.groupby(s):
        if len(list(v)) < 2:
            return_data.append(k)
    return return_data

def solution2(s):
    s = list(s)
    result = [s.pop(0)]
    while len(s) > 0:
        print(s)
        print(result)
        arr_start = s.pop(0)
        if len(result) < 1:
            result.append(arr_start)
            continue
        result_last = result.pop()

        if result_last != arr_start:
            result.append(result_last)
            result.append(arr_start)
    return 0 if len(result) > 0 else 1

arr1 = ['baabaa', 'cdcd']
return_list = [1, 0]
for i in range(len(arr1)):
    if solution2(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))