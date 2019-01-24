# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
#  예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
#
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.


def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n //= 10

    # return list(map(int, reversed(str(n))))
    return answer

arr = [12345]
return_list = [[5,4,3,2,1]]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 5 min