import numpy as np

N, M = map(int, input().split())
X = []
X.append(list(map(int, input().split())))
X.append(list(map(int, input().split())))
ans = 0

if sum(X[1]) != N:
    ans = -1
    print(ans)
    exit()

def arit(a1, an, n):
    return n * (a1 + an) // 2

if X[0][0] > 1:
    print(-1)
    exit()

diff = []
for i in range(M - 1):
    diff.append(X[0][i + 1] - X[0][i])
diff.append(N - X[0][-1] + 1)

for i in range(M):
    if diff[i] > X[1][i]:
        ans = -1
        break
    else:
        ans += arit(1, X[1][i] - 1, X[1][i] - 1)
        if i < M - 1:
            X[1][i + 1] += X[1][i] - diff[i]
            ans -= (arit(1, X[1][i] - diff[i], X[1][i] - diff[i]) - (X[1][i] - diff[i]))
print(ans)