N = int(input())
A = list(map(int, input().split()))
ans = 0

r = 1
for l in range(N):
    while r < N:
        if A[l] * 2 <= A[r]:
            ans += N - r
            break
        r += 1

print(ans)
    