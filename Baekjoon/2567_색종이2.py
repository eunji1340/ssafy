paper = [[0] * 100 for _ in range(100)]
N = int(input())

for n in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

ct = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < 100 and 0 <= nj < 100) or paper[ni][nj] == 0:
                    ct += 1

print(ct)
