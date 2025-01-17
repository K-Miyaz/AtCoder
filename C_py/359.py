S = list(map(int, input().split()))
T = list(map(int, input().split()))
width = abs(T[0] - S[0])
high = abs(T[1] - S[1])
ans = high

if T[0] > S[0]:
    if S[0] % 2 == S[1] % 2:
        if high + 1 < width:
            width -= (high + 1)
            ans += width // 2 + width % 2
    else:
        if high < width:
            width -= high
            ans += width // 2 + width % 2
else:
    if S[0] % 2 == S[1] % 2:
        if high < width:
            width -= high
            ans += width // 2 + width % 2
    else:
        if high + 1 < width:
            width -= (high + 1)
            ans += width // 2 + width % 2

print(ans)