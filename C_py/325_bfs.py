from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))
ans = 0
q = deque()

# 配列外参照をしないかチェック
def check(x, y):
    return 0 <= x < H and 0 <= y < W

def bfs_sensor(x, y):
    S[x][y] = "."
    # 周囲のマスにセンサーがあるかチェック
    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            nx, ny = x + i, y + j
            if check(nx, ny):
                if S[nx][ny] == "#":
                    q.append((nx, ny))
                    S[nx][ny] = "."
    while q:
        next_x, next_y = q.popleft()
        bfs_sensor(next_x, next_y)

for x in range(H):
    for y in range(W):
        if S[x][y] == "#":
            ans += 1
            bfs_sensor(x, y)

print(ans)