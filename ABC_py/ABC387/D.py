from collections import deque

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            sx, sy = i, j
        if S[i][j] == "G":
            gx, gy = i, j

Q = deque()
Q.append([sx, sy, 0, 0])
dirc_y = [(0, 1), (0, -1)]
dirc_x = [(1, 0), (-1, 0)]

while len(Q) > 0:
    x, y, l, j = Q.popleft()
    if l >= 0:
        for dx, dy in dirc_y:
            x2 = x + dx
            y2 = y + dy
            if not (0 <= x2 < H and 0 <= y2 < W):
                continue
            if S[x2][y2] == "#":
                continue
            if x2 == gx and y2 == gy:
                print(j + 1)
                exit()
            Q.append([x2, y2, -1, j + 1])
    if l <= 0:
        for dx, dy in dirc_x:
            x2 = x + dx
            y2 = y + dy
            if not (0 <= x2 < H and 0 <= y2 < W):
                continue
            if S[x2][y2] == "#":
                continue
            if x2 == gx and y2 == gy:
                print(j + 1)
                exit()
            Q.append([x2, y2, 1, j + 1])
print(-1)