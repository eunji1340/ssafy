# 아래 함수를 수정하시오.
def check_number(num):
    if num > 0 :
        print('양수입니다.')
    elif num == 0:
        print('0입니다.')
    else:
        print('음수입니다.')

while(True):
    try:
        num = int(input('숫자를 입력하세요 : '))
        check_number(num)
    except ValueError:
        print('잘못된 입력입니다.')
        break
