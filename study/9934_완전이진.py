def inorder(start, end, depth):
    if start > end:
        return

    mid = (start + end) // 2
    tree[depth].append(order[mid])

    inorder(start, mid - 1, depth + 1)
    inorder(mid + 1, end, depth + 1)

K = int(input())
order = list(map(int, input().split()))
tree = [[] for _ in range(K)]

inorder(0, len(order) - 1, 0)

for row in tree:
    print(*row)