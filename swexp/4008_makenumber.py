def cal(num, idx, pl, mi, mu, di):
    global min_num, max_num

    if idx == N:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        return

    if pl:
        cal(num + num_arr[idx], idx + 1, pl - 1, mi, mu, di)
    if mi:
        cal(num - num_arr[idx], idx + 1, pl, mi - 1, mu, di)
    if mu:
        cal(num * num_arr[idx], idx + 1, pl, mi, mu - 1, di)
    if di:
        cal(num // num_arr[idx] if num > 0 else -(-num // num_arr[idx]), idx + 1, pl, mi, mu, di - 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op = list(map(int, input().split()))
    num_arr = list(map(int, input().split()))
    min_num = float('inf')
    max_num = float('-inf')
    cal(num_arr[0], 1, *op)
    print(f'#{tc} {max_num - min_num}')