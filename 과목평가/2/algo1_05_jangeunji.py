T = int(input())  # 팀 수 (테스트케이스)
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N명의 팀원, M번의 명령
    arr = [0] + list(map(int, input().split()))  # 초기 상태. 앞에 인덱스를 추가해서 번호 맞추기
    for m in range(M):  # 명령 시행
        a, b, c = map(int, input().split())  # 난이도, 기준 번호, 사람 수
        for i in range(b, b+c):  # b번부터 b+c-1번까지 수행
            if i <= N:  # 총 인원 수 보다 작거나 같을 때 까지만
                arr[i] = (arr[i] + 1) % 2  # 상태를 0 -> 1, 1 -> 0 으로 바꾸기

    print(f'#{tc} {" ".join(map(str, arr[1:]))}')  # 0번 인덱스 제외하고 출력

