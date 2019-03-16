# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# 17	3
# 011	2
# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
#
# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
#
# 11과 011은 같은 숫자로 취급합니다.
from itertools import permutations


def solution(numbers):
    answer = 0

    return answer

def solution2(numbers):
    answer = 0
    candidates, num_set = [], set()
    digits = list(numbers)

    for i in range(1, len(numbers) + 1):
        # print(list(permutations(digits, i)))
        candidates += list(permutations(digits, i))
        # print(candidates)

    for candidate in candidates:
        # print(type(candidate))
        num_set.add(int(''.join(candidate)))
        # print(num_set)

    for num in num_set:
        if is_prime(num):
            answer += 1

    return answer


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True

arr1 = ['17', '011']
return_list = [3, 2]
for i in range(len(arr1)):
    if solution2(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# not pass