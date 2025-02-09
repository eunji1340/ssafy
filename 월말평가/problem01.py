############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    Sum = 0 # 총 합을 저장할 변수
    Max = weekly_like_list[0] # 가장 많은 좋아요 수를 저장할 변수. 초기값은 리스트의 첫번째 값
    Min = weekly_like_list[0] # 가장 적은 좋아요 수를 저장할 변수. 초기값은 리스트의 첫번째 값

    for num in weekly_like_list:
        Sum += num    # 총 합 변수에 수를 하나씩 더한다.
        if num > Max: # 초기값보다 num 값이 크면 Max에 num 값을 저장
            Max = num
        if num < Min: # 초기값보다 num 값이 작으으면 Min에 num 값을 저장
            Min = num

    aver = Sum / 7    # 평균값 계산
    return aver, Max-Min

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)
print(analyze_likes([7, 1, 2, 3, 4, 5, 6]))   # (7.0, 0)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
