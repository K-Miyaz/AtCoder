from itertools import permutations

N, K = map(int, input().split())
S = input()

ans = 0
for p in set(permutations(S)):
    t = "".join(p)
    ok = 1
    for i in range(N - K + 1):
        if t[i: i + K]== t[i: i + K][::-1]:
            ok = 0
    ans += ok
print(ans)