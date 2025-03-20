def dfs(idx, result, pl, mi, mu, di):
    global min_result, max_result

    if idx == N:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    if pl:
        dfs(idx + 1, result + num_arr[idx], pl - 1, mi, mu, di)
    if mi:
        dfs(idx + 1, result - num_arr[idx], pl, mi - 1, mu, di)
    if mu:
        dfs(idx + 1, result * num_arr[idx], pl, mi, mu - 1, di)
    if di:
        if result < 0:
            dfs(idx + 1, -(-result // num_arr[idx]), pl, mi, mu, di - 1)
        else:
            dfs(idx + 1, result // num_arr[idx], pl, mi, mu, di - 1)
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 숫자 개수
    oper_num = list(map(int, input().split()))  # 각 연산자 개수 (+-*/)
    num_arr = list(map(int, input().split()))  # N개의 숫자
    max_result = float('-inf')
    min_result = float('inf')
    dfs(1, num_arr[0], *oper_num)

    print(f'#{tc} {max_result - min_result}')