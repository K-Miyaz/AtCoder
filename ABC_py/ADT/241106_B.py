N, L, R = map(int, input().split())
A = [i for i in range(1, N + 1)]
for i in range(L - 1):
    print(A[i], end=" ")
for i in range(R + 1 - L):
    print(A[R - 1 - i], end= " ")
for i in range(R, N):
    print(A[i], end= " ")