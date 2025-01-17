N, M = map(int, input().split())
AB = [map(str, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*AB)]
F = [0] * N

for i in range(M):
    an = int(A[i]) - 1
    if B[i] == "F":
        print("No")
    elif F[an] == 0:
        F[an] += 1
        print("Yes")
    else:
        print("No")