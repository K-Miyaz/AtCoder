import itertools

N, K = map(int, input().split())
S = input()
s = list(S)
ans = 0
p = list(itertools.permutations(s, N))

for i in range(len(p)):
    ok = True
    for j in range(N - K):
        for k in range(K):
            if s[i][j + k] == s[i][j + K - k - 1]:
                ok = False
            else:
                ok = True
        if ok == False:
            break
    if ok == True:
        ans += 1

print(ans)