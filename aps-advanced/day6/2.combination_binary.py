arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1

for tar in range(1 << n):
    get_sub(tar)
    print()
