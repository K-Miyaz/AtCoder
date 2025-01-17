N, T = map(int, input().split())
A = list(map(int, input().split()))
ver = [0] * N
hor = [0] * N
dia = [0] * 2
ans = -1

for i in range(T):
    x = (A[i] - 1) % N
    y = (A[i] - 1) // N
    ver[x] += 1
    hor[y] += 1
    if x == y:
        dia[0] += 1
    if N - y - 1 == x:
        dia[1] += 1
    for j in range(N):
        if ver[j] == N or hor[j] == N:
            ans = i + 1
    for j in range(2):
        if dia[j] == N:
            ans = i + 1
    if ans > 0:
        break

print(ans)