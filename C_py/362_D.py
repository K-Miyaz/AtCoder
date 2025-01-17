N, M = map(int, input().split())
A = list(map(int, input().split()))

route = [[] for _ in range(M)]
for _ in range(M):
    u, v, w = map(int, input().split())
    route[u - 1].append((v - 1, w))
    route[v - 1].append((u - 1, w))

