N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse = True)
B = list(map(int, input().split()))
B.sort(reverse=True)
a = 0; b = 0

for i in range(N):
    a += A[i]; b += B[i]
    if (a > X) or (b > Y):
        break

print(i + 1)