# 문제 설명
# Finn은 요즘 수학공부에 빠져 있습니다.
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
#
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
#
# 제한사항
# n은 10,000 이하의 자연수 입니다.
# 입출력 예
# n	result
# 15	4
# 입출력 예 설명
# 입출력 예#1
# 문제의 예시와 같습니다.

def solution(n):
    answer = 0
    answer_list = []

    for i in range(1, n+1):
        answer_list_tmp = answer_list.copy()
        for a in answer_list_tmp:
            if a + i == n:
                answer += 1
                answer_list.remove(a)
            elif a + i > n:
                answer_list.remove(a)
            else:
                answer_list.remove(a)
                answer_list.append(a + i)
        answer_list.append(i)
        if i == n:
            answer+=1
    return answer
    # return len([i for i in range(1,n+1,2) if n % i is 0])

arr1 = [15]
return_list = [4]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))