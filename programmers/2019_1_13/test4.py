# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
#
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if check_prime(i): answer += 1
    return answer

def check_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i == 0:
            return False
    return True

#     num=set(range(2,n+1))
#
#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)

arr = [11, 5]
return_list = [5, 3]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 20 min