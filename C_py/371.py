from itertools import permutations

N = int(input())
Mg = int(input())
ver1 = [[0] * N for _ in range(N)]
for _ in range(Mg):
    u, v = map(int, input().split())
    ver1[u - 1][v - 1] = ver1[v - 1][u - 1] = 1
Mh = int(input())
ver2 = [[0] * N for _ in range(N)]
for _ in range(Mh):
    a, b = map(int, input().split())
    ver2[a - 1][b - 1] = ver2[a - 1][b - 1] = 1
A = []
for i in range(N - 1):
    row = list(map(int, input().split()))
    A.append([0] * (i + 1) + row)

ans = 10 ** 9
for p in permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if ver1[p[i]][p[j]] ^ ver2[i][j]:       # 片方だけ違うときTrue
                cost += A[i][j]
    ans = min(ans, cost)
    
print(ans)
