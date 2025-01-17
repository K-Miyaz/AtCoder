N = int(input())
A = list(map(int, input().split()))
a = []
A.sort(reverse=True)
for i in range(N):
    a.append((N - 1) * A[i])
l = 0
r = N - 1
count = 0
while l < r:
    if A[l] + A[r] >= pow(10, 8):
        count += r - l
        l += 1
    else:
        r -= 1
ans = sum(a) - pow(10, 8) * count
print(ans)