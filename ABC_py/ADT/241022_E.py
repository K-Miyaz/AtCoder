S = input()
N = len(S)
S = sorted(S)
def sigma(x):
    return x * (x + 1) // 2

ans = sigma(N - 1)
s = S[0]
slen = 0
for i in range(1, N):
    if s == S[i]:
        slen += 1
    else:
        ans -= sigma(slen)
        if slen > 0:
            ans += 1
        s = S[i]
        slen = 0
if slen > 0:
    ans -= sigma(slen) - 1
print(ans)
