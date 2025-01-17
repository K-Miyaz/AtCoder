import numpy as np
from numpy.linalg import solve

N, M = map(int, input().split())
uvw = [map(int, input().split()) for _ in range(M)]
u, v, w = [list(i) for i in zip(*uvw)]
A = np.zeros((N, M))
for i in range(M):
    A[i][v[i] - 1] = 1
    A[i][u[i] - 1] = -1

x = np.solve(A, w)
print(x)