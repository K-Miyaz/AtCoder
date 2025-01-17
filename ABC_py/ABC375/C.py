N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))
B = A
for i in range(N//2):
    for x in range(N - i):
        for y in range(N - i):
            B[y][N - x - 1] = A[x][y]
    A = B
for i in range(N):
    