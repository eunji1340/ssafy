K = int(input())

def find(k):
    if k == 1:
        return 0

    length = 1
    while length < k:
        length *= 2
    mid = length // 2

    if k == mid:
        return 0
    elif k < mid:
        return find(k)
    else:
        mirrored = length - k + 1
        return 1 - find(mirrored)

print(find(K))
