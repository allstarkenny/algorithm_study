# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
#
# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.
def solution(x, n):
    if x == 0: return [0 for _ in range(n)]
    return [i for i in range(x, x + n * x, x)]

# return [i * x + x for i in range(n)]

arr1 = [2, 4, -4, 0]
arr2 = [5, 3, 2, 0]
return_list = [[2,4,6,8,10], [4,8,12], [-4, -8], []]
for i in range(len(arr1)):
    if solution(arr1[i], arr2[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 9 min