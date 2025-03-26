for tc in range(1, 11):
    dump = int(input())  # 덤프 횟수
    box_height = list(map(int, input().split()))  # 상자들의 높이
    count = [0] * (101)  # 상자들의 높이 개수

    for i in range(100):
        count[box_height[i]] += 1


    for _ in range(dump):
        left = 0
        right = 100

        while left < 100 and count[left] == 0:
            left += 1

        while right > 0 and count[right] == 0:
            right -= 1

        count[left] -= 1
        count[left+1] += 1
        count[right] -= 1
        count[right-1] += 1

    left = 0
    right = 100

    while count[left] == 0:
        left += 1
    while count[right] == 0:
        right -= 1

    result = right - left

    print(f'#{tc} {result}')
