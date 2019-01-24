# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 입출력 예
# s	return
# try hello world	TrY HeLlO WoRlD

def solution(s):
    answer = ''
    print(s.split(' '))
    for word in s.split(' '):
        for idx, w in enumerate(word):
            answer += w.upper() if idx % 2 == 0 else w.lower()
        answer += ' '
    print(answer)
    return answer[:-1]

# return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

arr = ['try hello   world   ']
return_list = ['TrY HeLlO   WoRlD   ']

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 8 min