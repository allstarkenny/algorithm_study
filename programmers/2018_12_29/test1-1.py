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
import time


def solution(N, number):
    answer = 0
    # cal_formula('', 10, ['+', '-', '*', '/', ''])
    answer = get_formula(N, number)

    return answer


def get_formula(N, number):
    answer_list = []
    formula_list = []
    param_list = ['+', '-', '*', '/', '']
    bucket_cnt = 0

    make_formula(N, number, 1, '', answer_list, formula_list, param_list, bucket_cnt, True)
    print(answer_list)
    print(formula_list)
    return min(answer_list)


def make_formula(N, number, depth, formula, answer_list, formula_list, param_list, bucket_cnt, do_bucket):
    local_formula = formula
    local_bucket_cnt = bucket_cnt
    if len(answer_list) > 100:
        return

    local_formula += str(N)
    if cal_formula(local_formula + ''.join([')' for _ in range(local_bucket_cnt)]), number):
        print('find ! {}, {} = {}'.format(depth, local_formula + ''.join([')' for _ in range(local_bucket_cnt)])
                                          , number))
        answer_list.append(depth)
        formula_list.append(local_formula + ''.join([')' for _ in range(local_bucket_cnt)]))
        return

    if len(answer_list) > 0:
        if depth >= min(answer_list)-1:
            return
    elif depth > 7:
        return

    for i in range(2):
        local_bucket_str = ''
        if i == 1:
            if do_bucket:
                local_formula = local_formula[:-1]
                local_formula += '('
                local_formula += str(N)
                local_bucket_cnt += 1
                # print('append! {}'.format(local_bucket_cnt))
            else:
                continue

        test_bucket_cnt = local_bucket_cnt
        for j in range(local_bucket_cnt + 1):
            if j != 0 and i != 1:
                local_bucket_str += ')'
                test_bucket_cnt -= 1

            for param in param_list:
                if local_bucket_str != '' and param == '':
                    continue
                # print('param {} {} {} {} {} {}'.format(param, local_formula, depth, i, j, test_bucket_cnt))
                make_formula(N, number, depth+1, local_formula + local_bucket_str + param, answer_list,
                             formula_list, param_list, test_bucket_cnt, False if param == '' else True)
            # print('end_loop---------------------------------')


def cal_formula(formula, number):
    ch_formulas = chage_formula(formula)
    result = calc_formula(ch_formulas)
    if result == number:
        return True
    return False


def tokenize_formula(formula):
    OP = ("*", "/", "+", "-", "(", ")")
    before_num = ''
    result_list = []
    for f in formula:
        if f in OP:
            if before_num != '':
                result_list.append(before_num)
            result_list.append(f)
            before_num = ''
        else:
            before_num += f
    if before_num != '':
        result_list.append(before_num)
    return result_list


def chage_formula(formula):
    tokenized_formula = tokenize_formula(formula)
    OP = ("*", "/", "+", "-", "(", ")")
    P = {
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1,
        "(": 0
    }
    output = []
    stack = []

    for item in tokenized_formula:
        if item not in OP:
            output.append(item)
        elif item == "(":
            stack.append(item)
        elif item == ")":
            while stack != [] and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack != [] and P[stack[-1]] >= P[item]:
                output.append(stack.pop())
            stack.append(item)

    while stack:
        output.append(stack.pop())

    return output


def calc_formula(formula):
    OP = ("*", "/", "+", "-",)
    FUNC = {
        "*": lambda x, y: y * x,
        "/": lambda x, y: y // x,
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
    }
    stack = []

    for item in formula:
        if item not in OP:
            stack.append(int(item))
        else:
            x = stack.pop()
            y = stack.pop()
            try:
                stack.append(FUNC[item](x, y))
            except:
                return -1

    return stack.pop()


n_list = [5, 2, 5, 5, 5]
number_list = [12, 11, 25, 23, 27]
return_list = [4, 3, 2, 5, 5]

for i in range(len(n_list)):
    if solution(n_list[i], number_list[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))
