# 1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
# 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요.
# (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)
#
# 제한사항
# 표(board)는 2차원 배열로 주어집니다.
# 표(board)의 행(row)의 크기 : 1000 이하의 자연수
# 표(board)의 열(column)의 크기 : 1000 이하의 자연수
# 표(board)의 값은 1또는 0으로만 이루어져 있습니다.
import itertools

def solution(board):
    print(board)
    answer = 1234
    if 1 not in itertools.chain.from_iterable(board):
        return 0

    width = len(board[0])
    height = len(board)

    size = width if height > height else height

    print('{} {} {}'.format(width, height, size))
    for s in range(2, size+1):
        size_find = False
        print(s)
        for i in range(width - s + 1):
            print(width - s + 1)
            print(i)
            for j in range(height - s + 1):
                print('height - s + 1 = {}'.format(height - s + 1))
                print(j)
                zero_find = False
                for n in range(s):
                    if 0 in board[j + n][i:i + s]:
                        zero_find = True
                        print('zero find')
                        break
                if not zero_find:
                    print('find answer {}'.format(s))
                    answer = s ** 2
                    size_find = True
                    break
            if size_find:
                break



    print(answer)

    return answer

arr1 = [[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]], [[0,0,1,1],[1,1,1,1]]]
return_list = [9, 4]
for i in range(len(arr1)):
    if solution(arr1[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))