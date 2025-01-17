N, C = map(int, input().split())
T = list(map(int, input().split()))
s = -C
ans = 0
for i in range(N):
    if T[i] - s >= C:
        ans += 1
        s = T[i]
print(ans)