T = int(input())
for tc in range(1, T+1):
    N, MIN, MAX = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    check = -1
    result = 100

    for i in range(N):
        score1 = scores[i]
        for j in range(i, N):
            score2 = scores[j]

            g1, g2, g3 = 0, 0, 0

            for score in scores:
                if score >= score2:
                    g1 += 1
                elif score >= score1:
                    g2 += 1
                else:
                    g3 += 1

            if MIN <= g1 <= MAX and MIN <= g2 <= MAX and MIN <= g3 <= MAX:
                result = min(result, max(g1, g2, g3) - min(g1, g2, g3))
                check = 1

    print(f'{tc} {result if check == 1 else check}')