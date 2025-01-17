N, M = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
X = []
for i in range(M):
    X.append([x[i], a[i]])

if sum(a) != N:
    ans = -1
    print(ans)
    exit()

X = sorted(X, key=lambda x: x[0])

def arit(a1, an, n):
    return n * (a1 + an) // 2

if X[0][0] > 1:
    print(-1)
    exit()

diff = []
for i in range(M - 1):
    diff.append(X[i + 1][0] - X[i][0])
diff.append(N - X[-1][0] + 1)

for i in range(M):
    if diff[i] > X[i][1]:
        ans = -1
        break
    else:
        ans += arit(1, X[i][1] - 1, X[i][1] - 1)
        if i < M - 1:
            X[i + 1][1] += X[i][1] - diff[i]
            ans -= (arit(1, X[i][1] - diff[i], X[i][1] - diff[i]) - (X[i][1] - diff[i]))
print(ans)