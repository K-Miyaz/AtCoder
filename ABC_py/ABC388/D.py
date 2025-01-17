N = int(input())
A = list(map(int, input().split()))
temp = 0
for i in range(N - 1):
    gift = (N - i - 1) * (i + 1) + temp
    print(gift)
    if A[i] >= gift:
        A[i] -= gift
        A[i + 1] += gift
        temp = 0
    else:
        A[i + 1] += A[i]
        temp = A[i] - gift
        A[i] = 0
print(A)