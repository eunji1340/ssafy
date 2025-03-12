path = []
used = [False] * 7

def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    # 만약 카드가 1~6까지 6개가 있다면
    for num in range(1, 7):
        if num in path:
            continue
        path.append(num)
        recur(cnt + 1)
        #path.pop()

recur(0)