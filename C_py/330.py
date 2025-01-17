D = int(input())
d_half_sqrt = int((D / 2) ** 0.5)
if d_half_sqrt == 0:
    d_half_sqrt = 1
d_sqrt = int(D ** 0.5)
if d_sqrt ** 2 < D:
    d_sqrt += 1
inf = 10 ** 12
ans = inf

i = d_sqrt
# 非負整数を自然数と勘違いしてやっていた
j_line = 1
while i >= d_half_sqrt:
    ok = False
    j = j_line - 1
    while j >= j_line -1:
        S = i ** 2 + j ** 2 - D
        if S > 0:
            ans = min(abs(S), ans)
            j_line = j
            break
        elif S == 0:
            ans = min(abs(S), ans)
            ok = True
            break
        else:
            ans = min(abs(S), ans)
            j += 1
    if ok:
        break
    i -= 1
print(ans)