def find_palin(n, arr):
    ct = 0    # 회문의 개수
    #가로
    for i in range(8):
        for j in range(8-n+1):
            string = arr[i][j:j+n]
            if string == string[::-1]:
                ct += 1

    #세로
    for j in range(8):
        for i in range(8-n+1):
            string = [arr[x][j] for x in range(i, i + n)]
            if string == string[::-1]:
                ct += 1
    return ct

for tc in range(1, 11):
    N = int(input())                     # 회문의 길이
    board = [input() for _ in range(8)]  # 8*8, 글자는 'A', 'B', 'C'
    print(f'#{tc} {find_palin(N, board)}')