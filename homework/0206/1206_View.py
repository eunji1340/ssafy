for tc in range(1, 11):
    N = int(input())  # 건물의 개수
    height = list(map(int, input().split()))  # N개의 건물 높이
    ct = 0  # 조망권이 확보된 세대의 수

    for i in range(2, N-2):
        if height[i] < max(height[i+j] for j in [-2, -1, 1, 2]):
            continue

        ct += height[i] - max(height[i+j] for j in [-2, -1, 1, 2])

    print(f'#{tc} {ct}')

# 강사님 코드
# for tc in range(1, 11):
#     N = int(input())
#     height = list(map(int, input().split()))
#     ct = 0
#
#     for i in range(2, N-2):
#         neighbor = height[i-2:i] + height[i+1:i+3]  # 바로 옆 이웃한 4개의 건물 리스트
#         neighbor_max = max(neighbor)  # 이웃한 건물 중 최대 높이
#         if height[i] > neighbor_max:
#             ct += height[i] - neighbor_max  # i번째 건물의 조망권 더하기
#
#     print(f'#{tc} {ct}')