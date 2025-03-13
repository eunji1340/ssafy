

def find_idx(arr):
    count = [0] * 10  # 0~9 숫자 등장 횟수 저장

    for i in range(len(arr)):  # 배열 길이 고려
        count[arr[i]] += 1

        # 🟢 트리플렛 체크 (같은 숫자 3개)
        if count[arr[i]] >= 3:
            return i + 1  # 플레이어가 몇 번째 턴에서 승리했는지 반환

        # 🔵 런 체크 (연속된 숫자 3개)
        for j in range(8):  # 0~7까지만 확인 (j, j+1, j+2 검사)
            if count[j] > 0 and count[j+1] > 0 and count[j+2] > 0:
                return i + 1  # 몇 번째 턴에서 승리했는지 반환

    return -1  # 베이비진이 없는 경우

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 플레이어 1과 2의 숫자 배열 생성
    p1 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    p2 = [arr[i] for i in range(len(arr)) if i % 2 == 1]

    p1_idx = find_idx(p1)
    p2_idx = find_idx(p2)

    # 승자 판별 로직 수정
    if p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
        result = 1
    elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
        result = 2
    else:
        result = 0  # 둘 다 베이비진이 없거나 동시에 승리할 경우 무승부

    print(f'#{tc} {result}')
