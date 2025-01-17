N = int(input())
A = list(map(int, input().split()))
ans = N
l = 0
if N == 1:
    print(1)
    exit()
d = A[1] - A[0]
for i in range(1, N):
    if d == A[i] - A[i - 1]:
        l += 1
    else:
        for j in range(1, l + 1):
            ans += j
        d = A[i] - A[i - 1]
        l = 1
for j in range(1, 1 + l):
    ans += j
print(ans)