############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    Sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Sum = matrix[i][j-1] + matrix[i][j] + matrix[i][j+1] + matrix[i-1][j] + matrix[i+1][j]


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

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
