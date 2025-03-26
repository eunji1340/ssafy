used = [0] * 6
path = []
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):
        cnt += 1

    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b - 1) == (c - 2):
        cnt += 1

    return cnt == 2

def recur(cnt):
    global baby_gin_result
    if cnt == 6:
        baby_gin_result = is_baby_gin()

    for idx in range(6):
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0

arr = [6,6,7,7,6,7]
recur(0)

print('YES') if baby_gin_result else print('NO')