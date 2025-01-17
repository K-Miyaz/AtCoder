N, Q = map(int, input().split())
HT = [map(str, input().split()) for _ in range(Q)]
H, T = [list (i) for i in zip(*HT)]
L, R = 1, 2
ans = 0

for i in range(Q):
    t = int(T[i])
    if t == L or t == R:
        continue
    if H[i] == "R":
        if L < R and t > L:
            ans += abs(t - R)
        elif L < R and t < L:
            ans += N - R + t
        elif L > R and t > L:
            ans += R + N - t
        else:
            ans += abs(R - t)
        R = t
    else:
        if R < L and t > R:
            ans += abs(t - L)
        elif R < L and t < R:
            ans += N - L + t
        elif R > L and t > R:
            ans += L + N - t
        else:
            ans += abs(L - t)
        L = t
    # print("L={} R={} ans={}".format(L, R, ans))
print(ans)