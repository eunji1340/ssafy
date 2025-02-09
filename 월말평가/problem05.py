############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def count_happy(diary):
    ct = 0 # 마지막에 반환할 값. 단어가 등장한 횟수

    # happy의 글자 수가 5개이기 때문에 diary의 길이에서 4를 뺀 값까지만 돌린다
    for i in range(len(diary)-4): 
        if diary[i:i+5] == 'happy': # diary에서 5개의 글자를 빼와서 happy와 맞는지 확인
            ct += 1

    return ct
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_happy("I feel happy. HAPPY! so happy!"))  # 2
print(count_happy("happyhappy"))                      # 2
print(count_happy("nothing here"))                    # 0
#####################################################