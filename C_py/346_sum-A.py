import random
R = random.randint(1, 1 << 60)

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set([i ^ R for i in A]) # hack を防ぐため、iの代わりにi^Rを用いる
ans = K * (K + 1) // 2
for j in S:
    i = j ^ R   # 元に戻す
    if i <= K:
        ans -= i

print(ans)