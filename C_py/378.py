N = int(input())
A = list(map(int, input().split()))
B = [-1] * N
last = {}

for i in range(N):
    if A[i] in last:
        B[i] = last[A[i]]
    last[A[i]] = i + 1

print(*B)
