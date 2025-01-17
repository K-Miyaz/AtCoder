N, M = map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
a, b = [list(i) for i in zip(*ab)]
ans = N**2 - M

def take(x, y):
    lr, tu = 0, 0
    if x == 1:
        lr += 2
    if x == 2:
        lr += 1
    if x == (N - 1):
        lr += 2
    if x == (N - 2):
        lr += 1
    if y == 1:
        tu += 2
    if y == 2:
        tu += 1
    if y == (N - 1):
        tu += 2
    if y == (N - 2):
        tu += 1
    return 8 - tu

for i in range(M):
    L = take(a[i], b[i])
    ans -= L
    

