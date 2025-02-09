############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    # 리스트가 비어있는 경우에는 바로 값을 리턴한다다
    if items_list == []:
        return [], (0,0)
    
    check = items_list[0] # 중복된 값인지 확인하는 용도의 변수
    result = [] # 마지막에 반환할 리스트 변수

    for item in items_list:    # items_list를 돌면서 result 변수에 똑같은 값이 없다면 추가한다
        if item not in result:
            result.append(item)

    sum1 = 0 # 양수합 변수
    sum2 = 0 # 음수합 변수

    for num in result:
        if type(num) == int: # num 값이 int가 맞는지 확인
            if int(num) > 0: # 양수이면 sum1값에 더하고 아니라면 sum2에 더한다
                sum1 += num
            else:
                sum2 += num
    return result, (sum1, sum2)


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################

