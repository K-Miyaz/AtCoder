N = input()
d = len(N)
ans = 0

for i in range(2 ** d):
    R = []; L = []
    for j in range(d):
        if ((i >> j) & 1):
            R.append(N[j])
        else:
            L.append(N[j])
    R.sort(reverse=True)
    L.sort(reverse=True)
    if len(R) == 0 or len(L) == 0:
        r = 0
        l = 0
    else:
        r = int("".join(R))
        l = int("".join(L))
    ans = max(ans, r * l)

print(ans)