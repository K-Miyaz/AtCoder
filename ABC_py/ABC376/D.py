N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]
a = [[] for _ in range(N + 1)]
ans = -1

for i in range(M):
    a[ab[i][0]].append(ab[i][1])

def bfs(que):
    que