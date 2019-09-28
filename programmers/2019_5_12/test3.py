# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
#
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 입출력 예
# arr	result
# [2,6,8,14]	168

def solution(arr):
    answer = 1
    while len(arr) > 0:
        answer = lcm(answer, arr.pop())
    return answer

def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

def lcm(a, b):
    return a*b//gcd(a,b)

arr1 = [[2,6,8,14], [1,2,3]]
return_list = [168, 6]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))
