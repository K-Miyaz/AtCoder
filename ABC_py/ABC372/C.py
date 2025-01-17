N, Q = map(int, input().split())
S = input()
s = list(S)
XC = [map(str,input().split()) for _ in range(Q)]
X, C = [list(i) for i in zip(*XC)]
Scount = S.count
for i in range(Q):
    x = int(X[i])
    if C[i] == s[x -1]