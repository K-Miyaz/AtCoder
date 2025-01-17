N = int(input())
T = []
V = []
for i in range(N):
    t, v = map(int, input().split())
    T.append(t)
    V.append(v)
ans = V[0]
for i in range(1, N):
    ans -= T[i] - T[i - 1]
    if ans < 0:
        ans = 0
    ans += V[i]
print(ans)