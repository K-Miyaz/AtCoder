N, Q = map(int, input().split())
S = input()
s = list(S)
ans = S.count("ABC")

for _ in range(Q):
    x, C = map(str, input().split())
    X = int(x) - 1
    for i in range(X - 2, X + 1):
        if i >= 0:
            if s[i:i + 3] == ["A", "B", "C"]:
                ans -= 1
    s[X] = C
    for i in range(X - 2, X + 1):
        if i >= 0:
            if s[i:i + 3] == ["A", "B", "C"]:
                ans += 1
    print(ans)