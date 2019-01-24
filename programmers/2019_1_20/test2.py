# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
# z는 1만큼 밀면 a가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
#
# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

def solution(s, n):
    answer = ''
    small_char_list = []
    big_char_list = []

    for i in range(26):
        small_char_list.append(chr(ord('a') + i))
        big_char_list.append(chr(ord('A') + i))

    for c in s:
        if c in small_char_list:
            answer += small_char_list[(small_char_list.index(c) + n) % 26]
        elif c in big_char_list:
            answer += big_char_list[(big_char_list.index(c) + n) % 26]
        else:
            answer += c

    return answer


arr = ['AB', 'z', 'a B z']
n_list = [1, 1, 4]
return_list = ['BC', 'a', 'e F d']

for i in range(len(arr)):
    if solution(arr[i], n_list[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 12 min