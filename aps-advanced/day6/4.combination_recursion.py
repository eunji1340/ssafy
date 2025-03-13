# arr = list(range(1, 7))
# n = 3
#
# path = []
#
# def recur(cnt, start):
#     if cnt == n:
#         print(path)
#         return
#
#     for i in range(start, 7):
#         path.append(i)
#         recur(cnt + 1, i + 1)
#         path.pop()
#
#     for i in range(1, 7):
#         path.append(i)
#         recur(cnt + 1)
#         path.pop()
#
# recur(0, 1)


arr = list(range(1, 7))
path = []

n = 3

def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 6):
        path.append(arr[i])
        run(lev+1, i)
        path.pop()

run(0, 0)
