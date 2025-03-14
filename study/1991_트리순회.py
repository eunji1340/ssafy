def preorder(t):
    if t == '.':
        return

    print(t, end='')
    preorder(tree[t][0])
    preorder(tree[t][1])

def inorder(t):
    if t == '.':
        return

    inorder(tree[t][0])
    print(t, end='')
    inorder(tree[t][1])

def postorder(t):
    if t == '.':
        return

    postorder(tree[t][0])
    postorder(tree[t][1])
    print(t, end='')

N = int(input())
tree = {}
for _ in range(N):
    p, l, r = input().split()
    tree[p] = [l, r]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()