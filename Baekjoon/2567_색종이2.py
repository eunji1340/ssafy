paper = [[0] * 100 for _ in range(100)]
N = int(input())

for n in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] != 0:
                paper[i][j] = 2  # 겹친 부분은 2
            else:
                paper[i][j] = 1

for i in range(N):
    for j in range(N):
        ct = 0
        if paper[i][j] == 1 and (j - 1 == 0 or ):
            ct += 1
print(sum(row.count(1) for row in paper))
