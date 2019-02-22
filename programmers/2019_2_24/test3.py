# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다.
# 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

def solution(number, k):
    num_list = list(number)
    for _ in range(k):
        before_num = 0
        frist_num = int(''.join(num_list[:0]) + ''.join(num_list[1:]))
        for i in range(1, len(num_list)):
            second_num = int(''.join(num_list[:i]) + ''.join(num_list[i+1:]))
            print('{} -> {} {}'.format(''.join(num_list), frist_num ,second_num))

            if frist_num < second_num:
                frist_num = second_num
            elif second_num < frist_num:
                num_list = list(str(frist_num))
                break

            if i == len(num_list) - 1:
                num_list = list(str(second_num))
    print(''.join(num_list))
    return ''.join(num_list)


arr1 = ['1924', '1231234', '4177252841', '9876']
arr2 = [2,3,4, 2]
return_list = ['94', '3234', '775841', '98']
for i in range(len(arr1)):
    if solution(arr1[i], arr2[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 40 min x
