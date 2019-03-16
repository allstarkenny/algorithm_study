# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	6210
# [3, 30, 34, 5, 9]	9534330


def solution(numbers):
    answer = ''
    sorted_list = []
    for n in numbers:
        print(n)
        if len(sorted_list) < 1:
            sorted_list.append(str(n))
            continue
        for i, s in enumerate(sorted_list):
            # print('{} / {} = {} / {}'.format(i, s, i ,s[0]))

            if int(s[0]) < int(str(n)[0]):
                sorted_list.insert(i, str(n))
                break
            elif int(s[0]) == int(str(n)[0]):
                if check_same(str(n), s, s[0]):
                    sorted_list.insert(i, str(n))
                    break
            if i == len(sorted_list) - 1:
                sorted_list.append(str(n))
                break

    # print(sorted_list)
    answer = ''.join(sorted_list)

    return str(int(answer))

def check_same(input, comparison, same_num_str):
    max_len = len(input) if len(input) > len(comparison) else len(comparison)
    for _ in range(len(input), max_len):
        input += same_num_str
    for _ in range(len(comparison), max_len):
        comparison += same_num_str

    for i in range(1, max_len):
        if int(input[i]) > int(comparison[i]):
            return True
        elif int(input[i]) < int(comparison[i]):
            return False

    return True

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


arr1 = [[6, 10, 2], [3, 30, 34, 345, 5, 9], [9,90], [6,69]]
return_list = ['6210', '9534330', '990', '696']
for i in range(len(arr1)):
    if solution2(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))