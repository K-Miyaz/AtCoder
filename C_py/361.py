N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = [] * N
inf = 10 ** 9

i, j = -1, K
B_min = inf
while j >= 0 :
    B = A[i] - A[j]
    if B_min > B:
        B_min = B
    i -= 1
    j -= 1

print(B_min)