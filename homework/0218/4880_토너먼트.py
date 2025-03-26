def winner(l, r):
    global cards

    if l == r:
        return l

    mid = (l+r)//2
    left = winner(l, mid)
    right = winner(mid+1, r)

    if cards[left] == cards[right]:
        return left
    elif (cards[left] + 1) % 3 == cards[right] % 3:
        return right
    else:
        return left


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    print(f'#{tc} {winner(1, N)}')