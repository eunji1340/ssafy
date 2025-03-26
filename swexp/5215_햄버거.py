T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())  # 재료의 수, 제한 칼로리
    # 각 재료의 점수, 칼로리
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 점수는 높고, 칼로리는 낮은거
    for i in range(N):
        arr[i].insert(0, arr[i][0] / arr[i][1])  # 점수 / 칼로리
    arr.sort(reverse=True)  # 점수 오름차순 정렬

    def check_cal(arr):
        score = cal = i = 0
        while i < N:  # N개의 재료를 다 순회할 때까지
            # 칼로리를 더했을 때 제한칼로리를 초과했다면
            if cal + arr[i][2] > L:
                for j in range(i+1, N):  # 다음 재료들을 검사
                    # 만약 다음 재료 중에 더했을 때 제한 칼로리를 초과하지않으면
                    if cal + arr[j][2] <= L:
                        cal += arr[j][2]  # 더하고 브레이크
                        score += arr[j][1]
                        i = j + 1
                        break
                return score  # 중단

            score += arr[i][1]
            cal += arr[i][2]
            i += 1

    print(f'#{tc} {check_cal(arr)}')