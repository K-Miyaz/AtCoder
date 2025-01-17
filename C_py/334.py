N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**9
ans = INF
j = 0
diff_even = []
diff_odd = []
socks = []
c = [2] * (N + 1)
for a in A:
    c[a] = 1

for i in range(1, N + 1):
    for _ in range(c[i]):
        socks.append(i)

M = len(socks)
if K == 1:
    ans = 0
if K % 2 == 0:
    for i in range(0, len(A) - 1, 2):
        diff_even.append(A[i + 1] - A[i])
    ans = sum(diff_even)
else:
    for i in range(0, len(A) - 2, 2):
        diff_even.append(A[i + 1] - A[i])
    for i in range(1, len(A) - 1, 2):
        diff_odd.append(A[i + 1] - A[i])
    print(min(diff_even[i] + diff_odd[i + 1] for i in range(0, M, 2)))
print(ans)