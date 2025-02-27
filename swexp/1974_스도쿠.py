def check_num(puzzle):
    # 가로 검사
    for i in range(9):
        if len(set(puzzle[i])) != 9:
            return 0
    # 세로 검사
    for j in range(9):
        if len(set(puzzle[i][j] for i in range(9))) != 9:
            return 0
    # 작은 격자
    for I in range(0, 7, 3):
        for J in range(0, 7, 3):
            s = set()
            for i in range(3):
                for j in range(3):
                    s.add(puzzle[I+i][J+j])
            if len(s) != 9:
                return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]  # 9*9
    print(f'#{tc} {check_num(puzzle)}')
