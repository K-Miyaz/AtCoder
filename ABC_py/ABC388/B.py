N, D = map(int,input().split())
T = [0] * N; L = [0] * N
for i in range(N):
    T[i], L[i] = map(int, input().split())
for j in range(1, D + 1):
    ans = 0
    for i in range(N):
        ans = max(ans, T[i] * (L[i] + j))
    print(ans)