N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
a = A[0][0]
for i in range(1,N):
    a -= 1
    if a > i:
        a = A[a][i]
    else:
        a = A[i][a]
print(a)