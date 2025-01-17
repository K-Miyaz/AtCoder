import math

N = int(input())
XY = [map(int, input().split()) for _ in range(N)]
X, Y = [list (i) for i in zip(*XY)]
X.append(0); Y.append(0)
x = 0; y = 0
ans = 0

for i in range(N + 1):
    cost = 0
    cost = (x - X[i]) ** 2 + (y - Y[i]) ** 2
    cost = math.sqrt(cost)
    x = X[i]; y = Y[i]
    ans += cost
print(ans)