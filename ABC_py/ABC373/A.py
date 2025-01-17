S = []
ans = 0
for i in range(12):
    S.append(input())
for i in range(12):
    if (i+ 1) == len(S[i]):
        ans += 1
print(ans)