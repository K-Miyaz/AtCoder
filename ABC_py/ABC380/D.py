S = input()
Q = int(input())
K = list(map(int, input().split()))

for i in range(Q):
    k = K[i]
    slen = len(S)
    j = (k - 1) / slen
    while k < slen:
        slen *= 2

