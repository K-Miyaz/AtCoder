N, M = map(int, input().split())
A = list(map(int, input().split()))
Alist = list(map(int, input().split()))
ilist = [i for i in range(M)]
B = [[a, b] for a, b in zip(Alist, ilist)]

B.sort(reverse=True, key=lambda x: x[0])
j = 0

for i in range(M):
    while j < N:
        if A[j] <= B[i][0]:
            B[i][0] = j + 1
            break
        else:
            j += 1
    if j == N:
        B[i][0] = -1

B.sort(key=lambda x: x[1])
for i in range(M):
    print(B[i][0])