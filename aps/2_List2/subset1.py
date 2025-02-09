bit = [0] * 3
a = [2, 3, 7]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            s = 0
            for b in range(3):
                if bit[b]:
                    print(a[b], end=' ')  # 부분집합에 포함된 원소
                    s += a[b]
            print(bit, s)
