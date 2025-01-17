S = input()
s = sorted(list(S))
nows = S.index(s[0])
ans = 0

for i in range(len(S)):
    now = s[i]
    news = S.index(now)
    ans += abs(int(nows) - int(news))
    nows = int(news)
print(ans)