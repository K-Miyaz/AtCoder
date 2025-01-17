N = int(input())
qr = [map(int, input().split()) for _ in range(N)]
q, r = [list(i) for i in zip(*qr)]
Q = int(input())
td = [map(int, input().split()) for _ in range(Q)]
t, d = [list(i) for i in zip(*td)]

for i in range(Q):
    trs = t[i] - 1
    n = ((d[i] - r[trs] - 1) // q[trs]) + 1
    print(n * q[trs] + r[trs])