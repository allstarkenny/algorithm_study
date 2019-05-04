# 문제 설명
# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수,
# solution을 완성하세요.
# 예를들어 s가 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.
#
# 제한 조건
# s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
# 입출력 예
# s	return
# 1 2 3 4	1 4
# -1 -2 -3 -4	-4 -1
# -1 -1	-1 -1

def solution(s):
    t = [int(num) for num in s.split(' ')]
    answer = '{} {}'.format(str(min(t)),str(max(t)))
    # s = list(map(int,s.split()))
    return answer

arr1 = ['1 2 3 4', '-1 -2 -3 -4', '-1 -1']
return_list = ['1 4', '-4 -1', '-1 -1']
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))