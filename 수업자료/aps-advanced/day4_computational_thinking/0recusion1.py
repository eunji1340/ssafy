def KFC(num):
    if num == 5:
        return

    print(num)
    KFC(num + 1)  # 다음 재귀 호출
    KFC(num + 1)
    KFC(num + 1)
    KFC(num + 1)


KFC(0)
print("끝")