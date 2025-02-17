T = int(input())  # 테스트케이스
for tc in range(1, T+1):
    N = int(input())  # 괴물의 수
    arr = [list(map(int, input())) for _ in range(10)]  # 영역 정보

    for r in range(10):  # 행
        for c in range(10):  # 열
            if arr[r][c] in [1, 2, 3]:  # 만약 현재 위치 값이 1,2,3 중 하나라면 -> 괴물
                for dr, dc in [[0, 1], [-1, 0], [0, -1], [1, 0]]:  # 상하좌우 좌표 설정
                    for m in range(1, arr[r][c]+1):  # 괴물 인덱스 값만큼 레이저 발사
                        nr = r + dr * m  # 레이저가 비출 행의 위치
                        nc = c + dc * m  # 레이저가 비출 열의 위치

                        if 0 <= nr < 10 and 0 <= nc < 10:  # 경계조건 확인
                            if arr[nr][nc] in [1, 2, 3, 4]:  # 만약 벽이거나 다른 괴물이 있다면 break
                                break
                            arr[nr][nc] = 5  # 아니라면 5(레이저 표시)를 저장

    result = 0  # 안전한 구역의 수를 저장할 변수
    for a in arr:  # 2차원 배열에서 하나씩 확인
        result += a.count(0)  # 0(안전구역) 개수 세기
    print(f'#{tc} {result}')