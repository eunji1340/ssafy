import sys
sys.stdin = open("input.txt", "r")

def cal():
    global min_diff
    result = 0
    for i in range(N):
        for j in range(N):
            if i!=j:
                if selected[i] and selected[j]:
                    result += S[i][j]
                elif not selected[i] and not selected[j]:
                    result -= S[i][j]
    min_diff = min(abs(result), min_diff)
    return


def cook(idx, num):
    global N, S, min_diff, selected
    if num > N//2:
        return
    if idx == N-1:
        if num == N//2:
            cal()
        return

    cook(idx+1, num)

    selected[idx] = 1
    cook(idx+1, num+1)
    selected[idx] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    min_diff = 320000
    selected = [0]*N
    cook(0, 0)
    print(f"#{tc} {min_diff}")

# def cook(n):
#     global N, S, min_diff, selected
#     if n == N//2:
#         result1 = 0
#         result2 = 0
#         for i in range(N):
#             if selected[i]:
#                 for j in range(N):
#                     if selected[j] and i != j:
#                         result1 += S[i][j]
#                         result1 += S[j][i]
#             else:
#                 for j in range(N):
#                     if not selected[j] and i!=j:
#                         result2 += S[i][j]
#                         result2 += S[j][i]
#             min_diff = min(abs(result1-result2), min_diff)