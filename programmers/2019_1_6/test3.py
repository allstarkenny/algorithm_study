# 문제 설명
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때,
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
# 예를 들어 strings가 [sun, bed, car]이고 n이 1이면
# 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
#
# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.


def solution(strings, n):
    answer = []
    test_dict = {}
    for s in strings:
        if s[n] in test_dict.keys():
            test_dict[s[n]].append(s)
            test_dict[s[n]].sort()
        else:
            test_dict[s[n]] = [s]

    key_list = list(test_dict.keys())
    key_list.sort()

    for k in key_list:
        print(k)
        for i_k in test_dict[k]:
            answer.append(i_k)
    return answer

#   return sorted(strings, key=lambda x: x[n])

arr = [['sun', 'bed', 'car'],['abce', 'abcd', 'cdx']]
divisor = [1, 2]
return_list = [['car, bed, sun'], ['abcd', 'abce', 'cdx']]

for i in range(len(arr)):
    if solution(arr[i], divisor[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 18 min