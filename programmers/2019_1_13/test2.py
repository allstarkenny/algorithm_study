# 문제 설명
# 문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
# 예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
#
# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.

def solution(s):
    answer = True
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
# return s.isdigit() and len(s) in (4, 6)

arr = ['a234', '1234']
return_list = [False, True]

for i in range(len(arr)):
    if solution(arr[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 5 min
