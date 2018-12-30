# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.


def solution(N, number):
    answer = 0
    answer = make_formula(N, number)
    return answer

def make_formula(N, number):
    formula = str(N) + ' * ({}) / ' + str(N)
    inside_formula = []

    total_cnt = 0
    remove_divide = False

    if number % N != 0:
        total_cnt += 1
        print('number % N => total_cnt += 1 {}'.format(total_cnt))
    else:
        total_cnt = -1
        print('total_cnt = -1 {}'.format(total_cnt))
        remove_divide = True
        while number % N == 0:
            number = number // N
            formula = str(N) + " * " + formula
            total_cnt += 1
            print('formula = str(N) + " * " + formula total_cnt += 1 {}'.format(total_cnt))

    for i in range(2, 8):
        local_num = pow(N, i)
        if number - local_num < N and number - local_num > -1 * N:
            print('제곱으로 일부 표현 가능 {} - {} = {}'.format(number, local_num, str(number-local_num)))
            number -= local_num
            if number < 0:
                number *= -1
            total_cnt += i
            break

    loop_cnt = 0
    while number > 0:
        loop_cnt += 1
        local_divide = remove_divide
        for i in range(1, 7):
            if number < get_number(i):
                times = number // get_number(i - 1)
                if times > 6:
                    times = 11 - times
                    number -= get_number(i) - (get_number(i - 1) * times)
                    inside_formula.append('({} - ({} * {}))'.format(get_number(i), get_number(i - 1), times))

                    total_cnt += i
                    print('total_cnt += {} {}'.format(i, total_cnt))
                    total_cnt += (i - 1) * (times % N)
                    print('total_cnt += ({} - 1) * ({} % {}) {}'.format(i, times, N, total_cnt))

                    while times // N > 0:
                        times = times // N
                        if not local_divide:
                            total_cnt -= 1
                            print('times > 6 not local_divide total_cnt -= 1 {}'.format(total_cnt))
                            local_divide = True
                        else:
                            total_cnt += 1
                            print('times > 6 local_divide total_cnt += 1 {}'.format(total_cnt))
                else:
                    number -= get_number(i - 1) * times

                    inside_formula.append('( {} * {} )'.format(get_number(i - 1), times))

                    total_cnt += (i - 1) * (times % N)
                    print('total_cnt += ({} - 1) * ({} % {}) {}'.format(i, times, N, total_cnt))
                    while times // N > 0:
                        times = times // N
                        if not local_divide:
                            local_divide = True
                        else:
                            total_cnt += 1
                            print('times < 6 total_cnt += 1 {}'.format(total_cnt))
                break

        if loop_cnt > 8:
            return -1

        if total_cnt > 8:
            print('-1')
            return -1

    print(formula.format('+'.join(inside_formula)))
    print(str(total_cnt))
    return total_cnt

def get_number(times):
    return_number = 0
    for i in range(times):
        return_number += pow(10, i)
    return return_number

n_list = [5, 2, 5, 5, 5, 5]
number_list = [12, 11, 31168, 25, 23, 27]
return_list = [4, 3, -1, 2, 5, 5]

for i in range(len(n_list)):
    if solution(n_list[i], number_list[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))
