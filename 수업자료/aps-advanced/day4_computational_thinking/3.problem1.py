
path = []
result = 0

def recur(cnt, total):
    global result

    if total > 10:
        return

    if cnt == 3:
        if total <= 10:
            result += 1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1, total + num)
        path.pop()

recur(0, 0)
