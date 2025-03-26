# def count_string(str1, str2):
#     N = len(str1)
#     M = len(str2)
#
#     words = []
#     for i in range(N):
#         if str1[i] not in words:
#             words.append(str1[i])
#
#     result = 0
#     for word in words:
#         ct = 0
#         for i in range(M):
#             if str2[i] == word:
#                 ct += 1
#         if result < ct:
#             result = ct
#
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     print(f'#{tc} {count_string(str1, str2)}')

# 강사님 코드
T = int(input())

for tc in range(1, T+1):
    char_set = set([c for c in input().strip()])  # str1
    arr = [c for c in input().strip()]            # str2

    cnt = {}
    for c in char_set:
        cnt[c] = 0

        for ch in arr:
            if c == ch:
                cnt[c] += 1

    print(f'#{tc} {max(cnt.values())}')