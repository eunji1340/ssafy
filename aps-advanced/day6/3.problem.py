arr = ['A', 'B', 'C', 'D']
n = len(arr)

def get_sub(tar):
    global ct
    friend = []
    for i in range(n):
        if tar & 1:
            friend.append(arr[i])
        tar >>= 1
    if len(friend) >= 2:
        print(friend)
        ct += 1

ct = 0
for tar in range(1 << n):
    get_sub(tar)
print(ct)