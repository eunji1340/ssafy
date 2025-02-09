############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    Max = 0 # 최대값인지 확인하기 위한 변수
    x, y = 0, 0 # 마지막에 반환할 행, 열 값

    for i in range(len(matrix)): # matrix의 행
        for j in range(len(matrix[i])): # matrix의 열
            if matrix[i][j] > Max: # 최대값인지 확인 후에 변수에 행과 열 값을 저장
               Max = matrix[i][j]
               x, y = i, j

    return [x, y]
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
