def find_step(adj, A):
    global result

    check_number = list(range(1, N + 1))  # 체크할 사람 번호 리스트
    check_number.remove(A)  # 본인은 제외

    for B in check_number:
        visited = [0] * (N + 1)
        q = [A]
        visited[A] = 1
        while q:
            t = q.pop(0)
            for n in adj[t]:  # A의 인접리스트에서 하나씩 빼오기
                if n == B:  # B라면 단계더하고 다음 사람 검사하러
                    result[A] += visited[t]
                    q = []
                    print(result[A])
                    break
                else:  # B가 아니라면 q에 추가
                    q.append(n)
                    visited[n] += visited[t]

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]  # 인접리스트 생성, 무방향
# [[], [3, 4], [3], [1, 4, 2], [1, 5, 3], [4]]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

result = [0] * (N+1)  # 각 사람의 케빈 베이컨 수를 저장할 리스트
for i in range(1, N+1):
    find_step(adj, i)
print(result)
print(min(result))  # 가장 작은 수 출력

'''
from pprint import pprint
def bfs(i):
    front, rear = -1, 0
    visited = [0] * (N + 1)
    q = [0] * N
    q[rear] = i
    visited[i] = 1              
    while front < rear:
        front += 1
        r = q[front]
        for j in adj_matrix[r]:
            if j == 0:
                continue
            if not visited[j]:
                visited[j] = visited[r] + 1
                rear += 1
                q[rear] = j                 
    S = sum(visited)
    return S

N, E = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(E))

adj_matrix = [[0] * (N + 1) for _ in range(N + 1)]
S = [0] * (N + 1)

for s, e in edge:
    adj_matrix[s][e] = e
    adj_matrix[e][s] = s

pprint(adj_matrix)

for i in range(1, N + 1):
    S[i] = bfs(i)



m = min(S[1:])
for i in range(1, N + 1):
    if S[i] == m:
        break
print(i)
'''