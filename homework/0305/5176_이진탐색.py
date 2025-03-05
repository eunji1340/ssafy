# def pre_order(T):
#     global value, num
#     if T:
#         pre_order(left[T])
#         value[T] = num
#         num += 1
#         pre_order(right[T])
# 
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
# 
#     left = [0] * (N + 1)
#     right = [0] * (N + 1)
#     
#     for i in range(1, N//2+1):
#         left[i] = i * 2
#     for i in range(1, N//2 + N % 2):
#         right[i] = i * 2 + 1
#     
#     value = [0] * (N+1)
#     num = 1
#     pre_order(1)
#     
#     print(f'#{tc} {value[1]} {value[int(N/2)]}')

T = int(input())


# 중위순회
# 노드 번호 i가 주어졌을 때
# LVR
# 왼쪽 트리를 먼저 순회한다음
# 나를 체크하고
# 오른쪽 트리 순회하러감
def inorder(i):
    global cnt
    lft = 2 * i  # 왼쪽 자식 (배열의 인덱스 범위 안에 있다면)
    rgt = 2 * i + 1  # 오른쪽 자식

    # 왼쪽 트리 먼저 순회
    if lft <= N:  # 왼쪽 자식이 있다면
        inorder(lft)  # 왼쪽 자식을 기준으로 중위순회

    # 자기자신 순회 
    tree[i] = cnt
    cnt += 1

    # 오른쪽 트리 순회
    if rgt <= N:  # 오른쪽 자식이 있다면
        inorder(rgt)


for tc in range(1, T + 1):
    N = int(input())

    # 완전이진트리를 만들고
    # 번호를 이진탐색트리처럼 채워넣는다
    # (중위순회를 하면서 1부터 시작해서 번호를 채워넣는 문제).

    # 완전 이진 트리
    # - 루트 번호가 1부터 시작
    # - 위에서 부터 아래로, 왼쪽에서부터 오른쪽으로 채워넣는 트리
    # => 길이가 (N+1)을 배열을 만들고
    # 부모: i
    # - 왼쪽 자식: 2*i
    # - 오른쪽 자식: 2*i + 1

    # 자식: i
    # - 부모: i // 2

    tree = [0] * (N + 1)
    cnt = 1
    inorder(1)  # 루트 노드부터 중위순회를 한다.
    print(tree)
    print(f"#{tc} {tree[1]} {tree[N // 2]}")