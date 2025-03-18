arr = list(range(1, 11))
visited = []

def dfs(cnt, total, subset):
    if total == 10:
        print(subset)
        return

    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])
    dfs(cnt + 1, total, subset)

dfs(0, 0, [])

# ans = []
#
# for i in range(1 << len(arr)):
#     temp = []
#     for j in range(len(arr)):
#         if i & (1 << j):
#             temp.append(arr[j])
#             if sum(temp) > 10:
#                 break
#     if sum(temp) == 10:
#         ans.append(temp)
#
# print(ans)