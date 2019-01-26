# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
#
# 제한 조건
# num은 int 범위의 정수입니다.

def solution(num):
    answer = ['Odd', 'Even']
    return answer[(num + 1) % 2]

arr = [3, 4]
return_list = ['Odd', 'Even']

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 3 min