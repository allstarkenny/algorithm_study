# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.
#
# 제한 조건
# n은 길이 10,000이하인 자연수입니다.


def solution(n):
    answer = ''
    for _ in range(n // 2 + 1):
        answer += '수박'
    return answer[:n]

# return ("수박" * n)[:n]
# return "수박"*(n//2) + "수"*(n%2)


arr = [3, 4]
return_list = ['수박수', '수박수박']

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 8 min