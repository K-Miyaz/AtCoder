import math

L, M = map(int, input().split())
l = [list(map(int, input().split())) for i in range(M)]
l = sorted(l, key=lambda x: x[0])
x, y = 1, 1
ans = 0



for i in range(M):
    if y < l[i][0]:
        for j in range(y, l[i][0]):
            