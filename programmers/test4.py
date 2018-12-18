# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

def solution(s):
    answer = ''
    s_len = len(s)

    if s_len % 2 == 0:
        answer = s[int(s_len/2) - 1] + s[int(s_len/2)]
    else:
        answer = s[int(s_len / 2)]

    return answer
    # 아주 멋진 코드
    # return str[(len(str)-1)//2:len(str)//2+1]

s = ["abcde", "qwer"]
answer = ["c", "we"]

for i in range(len(s)):
    if solution(s[i]) == answer[i]:
        print('case {} pass'.format(str(i + 1)))
    else:
        print('case {} fail'.format(str(i + 1)))