from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
inf = 10 ** 9
d = [inf] * (N + 1)
q = deque()
for _ in range(M):
    a, b = map(int, input().split())        
    g[a].append(b)
    if a == 1:
        d[b] = 1
        q.append(b)

while q:
    x = q.popleft()
    for y in g[x]:
        if d[y] > d[x] + 1:
            d[y] = d[x] + 1
            q.append(y)

print(d[1] if d[1] < inf else -1)
