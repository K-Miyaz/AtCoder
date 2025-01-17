N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
temp = 0
r = A[1]
j = 0
for i in range(N):
    l = A[i]
    temp2 = 1
    while r - l < M:
        if r == l:
            temp2 += 1
        temp += 1
        j += 1
        if i + j >= N:
            break
        r = A[i + j]
    ans = max(ans, temp)
    temp -= temp2
print(ans)