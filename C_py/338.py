N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

INF = 10 **6 + 1
A_min = INF

for i in range(N):
    if A[i] > 0 and A_min > Q[i] // A[i]:
        A_min = Q[i] // A[i]

for x in range(A_min + 1):
    y = INF
    for i in range(N):
        if B[i] > 0:
            y = min(y, (Q[i] - A[i] * x) // B[i])
    ans = max(ans, x + y)
    
print(ans)