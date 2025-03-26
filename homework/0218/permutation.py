# 출력 배열 res에서 특정 자리(idx)의 숫자를 하나 채워넣고
# 그 다음 인덱스(idx+1) 뽑으러 가는 함수
# 재귀함수 : 기저조건, 유도조건
def perm(idx):
    if idx == R:
        # 순열이 완성
        print(res)
        return
    else:
        # N개의 숫자 중에서, 아직 뽑지 않은 수를
        # res의 idx번째에 집어 넣고
        # 그 다음 수 뽑으러 감.
        for i in range(N):  # arr의 i=0 ~ N-1의 모든 수를 검사
            if not visited[i]:  # 만약 아직 방문하지 않은 수라면
                visited[i] = True
                res[idx] = arr[i]  # i번째 수를 뽑아서 idx번째에 집어 넣는다.
                perm(idx+1)  # 그 다음 수를 뽑으러 감
                visited[i] = False  # 그 다음 i를 검사할 때는 방문체크를 초기화한 후 검사해야 함
                # 그래야 for문에서 앞의 작업이 그 다음 작업에 영향을 주지 않는다.

arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3

# 순열 : 같은 것을 다시 뽑으면 안됨
# -> 방문 체크 : 그 숫자를 썼는지 안썼는지 기억
visited = [False] * N  # 방문처리 배열
res = [0] * R  # 출력 배열

# 순열을 재귀함수로 설계
# R개의 수를 뽑아야 함 : 0번, 1번, .. , R-1번 인덱스까지 R번 숫자를 뽑는다.
perm(0)  # 0번 index 자리의 수를 뽑으러 감

