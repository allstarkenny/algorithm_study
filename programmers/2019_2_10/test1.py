# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
#
# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

import numpy as np

def solution(arr1, arr2):
    return np.add(arr1, arr2).tolist()
#     for i in range(len(A)) :
#         for j in range(len(A[0])):
#             A[i][j] += B[i][j]
#     return A


arr1 = [[[1,2],[2,3]], [[1],[2]]]
arr2 = [[[3,4],[5,6]], [[3],[4]]]
return_list = [[[4,6],[7,9]], [[4],[6]]]
for i in range(len(arr1)):
    if solution(arr1[i], arr2[i]) == return_list[i]:
        print('case {} pass --------------'.format(str(i + 1)))
    else:
        print('case {} fail --------------'.format(str(i + 1)))

# 10 min