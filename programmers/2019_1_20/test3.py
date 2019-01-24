# 문제 설명
# 자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 사항
# n은 0 이상 3000이하인 자연수입니다.

# def solution(n):
#     answer = 0
#
#     n_half = n // 2 + n % 2
#     n_list = []
#
#     for i in range(1, n_half):
#         if i not in n_list and n % i == 0:
#             answer += i
#             n_list.append(i)
#             answer += n // i
#             n_list.append(n//i)
#     print(answer)
#     return answer

def solution2(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

arr = [12, 5, 0]
return_list = [28, 6, 0]

for i in range(len(arr)):
    if solution2(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 10 min