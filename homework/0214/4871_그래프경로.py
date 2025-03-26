def dfs(adj, V, s, g):
    visited = [0] * (V+1)  # 방문 표시
    stack = []

    while True:
        if s == g:           # 현재 노드가 도착노드라면
            return 1

        if visited[s] == 0:  # 첫 방문 일 때
            visited[s] = 1

        for w in adj[s]:     # 인접하고 방문 안한 w 찾기
            if visited[w] == 0:
                stack.append(s)
                s = w
                break
        else:                # 더 이상 갈 곳이 없으면
            if stack:
                s = stack.pop()   # 이전 노드로 돌아가기
            else:                 # 스택이 비어 있다면
                break
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))  # 정점 개수, 간선 개수

    # 인접행렬 만들기
    adj = [[] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj[v1].append(v2)

    S, G = list(map(int, input().split()))  # 출발 노드, 도착 노드
    print(f'#{tc} {dfs(adj, V, S, G)}')