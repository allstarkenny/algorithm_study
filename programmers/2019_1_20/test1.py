# 문제 설명
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
#
# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 0으로 시작하지 않습니다.

def solution(s):
    answer = 0
    return int(s)

# def solution2(s):
#     num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     result = 0
#
#     for idx, number in enumerate(s[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += num_list.index(number) * (10 ** idx)
#
#     return result

arr = ['3123', '-4321']
return_list = [3123, -4321]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 2 min