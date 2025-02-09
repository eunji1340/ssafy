T = int(input())

for tc in range(1, T+1):
    N = int(input())
    string  = input()
    count = [0] * 10

    for s in string:
        count[int(s)] += 1

    card_number = 0
    card_count = 0
    for i in range(10):
        if card_count <= count[i]:
            card_count = count[i]
            card_number = i

    print(f'#{tc} {card_number} {card_count}')

