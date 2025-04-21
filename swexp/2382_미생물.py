T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 셀의 개수, 격리 시간, 군집의 개수
    # 세로 위치, 가로 위치, 미생물 수, 이동 방향
    micro_arr = [list(map(int, input().split())) for _ in range(K)]
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    def simula(now_micro, time):
        if time == M:
            return now_micro

        temp_map = {}
        for r, c, n, d in now_micro:
            nr, nc = r + dr[d], c + dc[d]

            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                n //= 2
                if d == 1 or d == 3:
                    d += 1
                else:
                    d -= 1

            if n == 0:
                continue

            if (nr, nc) not in temp_map:
                temp_map[(nr, nc)] = [[n, d]]
            else:
                temp_map[(nr, nc)].append(([n, d]))

        next_micro = []
        for (r, c), micro in temp_map.items():
            if len(micro) == 1:
                n, d = micro[0]
                next_micro.append([r, c, n, d])
            else:
                total_n = sum(x[0] for x in micro)
                max_n = -1
                direction = 0
                for n, d in micro:
                    if n > max_n:
                        max_n = n
                        direction = d
                next_micro.append([r, c, total_n, direction])

        return simula(next_micro, time + 1)

    result_arr = simula(micro_arr, 0)
    print(f'#{tc} {sum(x[2] for x in result_arr)}')