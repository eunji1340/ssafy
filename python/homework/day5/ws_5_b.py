data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

# 아래에 코드를 작성하시오.
for i in data_1:
    if i.isupper() == True or i == ' ':
        print(i, end = '')

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
for i in '내힘들다':
    arr.append(data_2.find(i))

print(arr)

arr.sort()
print(arr)

for i in arr:
    print(data_2[i], end='')