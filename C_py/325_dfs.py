from collections import deque

H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))
ans = 0
q = deque()

def check(x, y):
    return 0 <= x < H and 0 <= y < W

def dfs_sensor(x, y):
    S[x][y] = "."
    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            nx, ny = x + i, y + j
            if check(nx, ny):
                if S[nx][ny] == "#":
                    q.append((nx, ny))
                    S[nx][ny] = "."
    while q:
        next_x, next_y = q.pop()
        dfs_sensor(next_x, next_y)

for x in range(H):
    for y in range(W):
        if S[x][y] == "#":
            ans += 1
            dfs_sensor(x, y)

print(ans)