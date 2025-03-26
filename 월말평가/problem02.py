############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    result1 = {} # 보물 개수 딕셔너리 변수
    result2 = 0 # 임계값 이상을 초과하는 보물 종류 수 변수

    for i in range(len(treasure_list)):
        ct = 0 # 보물 개수를 저장하는 변수

        if treasure_list[i] not in result1.keys(): # result1에 보물이 저장이 되어있지않은 경우일 때
            for treasure in treasure_list: # treasure_list에 treasure가 있는지 확인하여 개수(ct)를 저장
                if treasure == treasure_list[i]:
                    ct += 1
            
            result1[treasure_list[i]] = ct # 딕셔너리 값 추가

        if ct > threshold: # 보물 개수가 임계값을 넘은 경우면 result2 값에 1을 더한다
            result2 += 1

    return result1, result2
         
            


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 테스트 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_treasures(["gold", "silver", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################
