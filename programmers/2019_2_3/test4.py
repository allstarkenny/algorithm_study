# 문제 설명
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 n을 입력받아 n이 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
#
# 제한 조건
# n은 1 이상, 10000 이하인 정수입니다.

def solution(x):
    return x % sum([int(s) for s in str(x)]) == 0

arr = [10, 12, 11, 13]
return_list = [True, True, False, False]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 5 min