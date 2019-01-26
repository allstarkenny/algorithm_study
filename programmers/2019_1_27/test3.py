# 임의의 정수 n에 대해, n이 어떤 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
#
# 제한 사항
# n은 1이상, 50000000000000 이하인 정수입니다.
import math

def solution(n):
    answer = 0

    # sqrt = n ** (1/2)

    if math.sqrt(n) % 1 == 0:
        return math.pow(int(math.sqrt(n)) + 1, 2)
    else:
        return -1

arr = [121, 3]
return_list = [144, -1]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 7 min