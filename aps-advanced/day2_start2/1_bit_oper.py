# print(1 << 1, bin(1 << 1))
# print(1 << 2, bin(1 << 2))
# print(1 << 3, bin(1 << 3))
# print(1 << 4, bin(1 << 4))
#
# print(7 >> 1, bin(7 >> 1))
#
# num = 1
# for _ in range(5):
#     print(num)
#     num = num << 1

arr = [1, 2, 3, 4]

for i in range(1 << len(arr)):  # i = 0~15
    for idx in range(len(arr)):  # idx = 0,1,2,3 반복
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()