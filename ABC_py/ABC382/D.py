N, M = map(int, input().split())
ans = []
def dic(i, j):
    if j < N:
        A.append(i)
        dic(i + 10, j + 1)
    while i < M:
        A.append(i)
        ans.append(A)
        A.pop(-1)
        i += 1
        
i = 0
while i < (M - (N - 1) * 10):
    A = []
    dic(i, i % 10)
    ans.append(A)
print(ans)
print(len(ans))