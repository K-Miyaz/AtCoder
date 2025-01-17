N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

A.append(0)
for i in range(Q):
    l = L[i] - 1
    if A[l] == N:
        continue
    if A[l] + 1 == A[l + 1]:
        continue
    else:
        A[l] = A[l] + 1

A.pop(K)
A = [str(i) for i in A]
print(" ".join(A))