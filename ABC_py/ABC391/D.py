N, W = map(int, input().split())
XY = [[] for _ in range(W)]
for _ in range(N):
    x, y = map(int, input().split())
    XY[x].append(y)

Q = int(input())
TA = [map(int, input().split()) for _ in range(Q)]
T, A = [list(i) for i in zip(*TA)]

