def check_binggo():
    global ct, row_checked, col_checked, diag_checked

    # 대각선
    if not diag_checked[0] and sum(binggo[i][i] for i in range(5)) == 0:
        diag_checked[0] = True
        ct += 1

    if not diag_checked[1] and sum(binggo[i][4-i] for i in range(5)) == 0:
        diag_checked[1] = True
        ct += 1
    
    # 가로
    for i in range(5):
        if not row_checked[i] and sum(binggo[i]) == 0:
            row_checked[i] = True
            ct += 1
                
    # 세로
    for i in range(5):
        if not col_checked[i] and sum(binggo[j][i] for j in range(5)) == 0:
            col_checked[i] = True
            ct += 1
        
binggo = [list(map(int, input().split())) for _ in range(5)]
number = []

for i in range(5):
    number.extend(list(map(int, input().split())))

ct = 0
row_checked = [False] * 5
col_checked = [False] * 5
diag_checked = [False] * 2

for num_i in range(25):
    num = number[num_i]
    
    for i in range(5):
        for j in range(5):
            if binggo[i][j] == num:
                binggo[i][j] = 0

    check_binggo()
    
    if ct >= 3:
        print(num_i+1)
        break