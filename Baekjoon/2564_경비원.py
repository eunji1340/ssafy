width, height = map(int, input().split())
block = [[0] * width for _ in range(height)]
n = int(input())

for i in range(n+1):
    dir, leng = map(int, input().split())
    if dir == 1:
        block[0][leng] = i + 1
    elif dir == 2:
        block[-1][leng] = i + 1
    elif dir == 3:
        block[leng][0] = i + 1
    elif dir == 4:
        block[leng][-1] = i + 1

for i in range(height):
    print(*block[i])
