N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = []
j = 0
for i in range(1, N + 1):
    if j == M:
        j = 0
    if A[j] == i:
        j += 1
    else:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i, end = " ")
print()
