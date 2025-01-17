N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
    if A[i] >= 0:
        ans += A[i]
    elif abs(A[i]) > ans:
        ans = 0
    else:
        ans += A[i]
print(ans)