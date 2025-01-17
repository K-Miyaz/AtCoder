N, K = map(int, input().split())
S = list(input())
ans = 0
ok = 0
for i in range(N):
    if S[i] == "O":
        ok += 1
        if ok >= K:
            ans += 1
            ok = 0
    else:
        ok = 0
print(ans)