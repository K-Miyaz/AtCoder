N, M = map(int, input().split())
k, S = [], []
for _ in range(M):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    S.append(ks[1:])
p = list(map(int, input().split()))

ans = 0

for mask in range(1 << N):
    ok = True
    for i in range(M):
        cnt = 0
        for s in S[i]:
            cnt += (mask >> (s - 1)) & 1
        ok &= cnt % 2 == p[i]
    ans += ok
print(ans)