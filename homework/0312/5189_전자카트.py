def per(ct, prev, energy):
    global min_energy

    if energy > min_energy:
        return

    if ct == N - 1:
        min_energy = min(min_energy, energy + energy_list[prev][0])
        return

    for i in range(1, N):
        if used[i]:
            continue
        used[i] = 1
        per(ct + 1, i, energy + energy_list[prev][i])
        used[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    energy_list = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    used[0] = 1
    min_energy = float('inf')
    per(0, 0, 0)

    print(f'#{tc} {min_energy}')