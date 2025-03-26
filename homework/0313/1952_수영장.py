import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    pay = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0] * 13

    for i in range(1, 13):
        # 1일 이용권 vs 1달 이용권 비교
        cost_day = dp[i - 1] + plan[i - 1] * pay[0]  # i-1 번째 인덱스가 i월을 의미
        cost_month = dp[i - 1] + pay[1]

        # 3달 이용권 고려 (i >= 3일 때만 적용 가능)
        if i >= 3:
            cost_3month = dp[i - 3] + pay[2]
        else:
            cost_3month = pay[2]

        # 현재 달의 최소 비용 선택
        dp[i] = min(cost_day, cost_month, cost_3month)

    result = min(dp[12], pay[3])

    print(f'#{tc} {result}')
