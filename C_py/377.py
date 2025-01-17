N, M = map(int, input().split())
S = set()
A = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [0, 0]]
for i in range(M):
    a, b = map(int, input().split())
    for i in A:
        if 1 <= a + i[0] <= N and 1 <= b + i[1] <= N:
            S.add((a + i[0], b + i[1]))
print(N * N - len(S))