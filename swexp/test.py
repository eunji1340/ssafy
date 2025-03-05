'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(T):
    if T:  # 0이 아니면
        print(T)
        pre_order(left[T])
        pre_order(right[T])

def in_order(T):
    if T:  # 0이 아니면
        in_order(left[T])
        print(T)
        in_order(right[T])

def post_order(T):
    if T:  # 0이 아니면
        post_order(left[T])
        post_order(right[T])
        print(T)


N = int(input())
E = N - 1
arr = list(map(int, input().split()))

left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

print(left)
print(right)

in_order(1)