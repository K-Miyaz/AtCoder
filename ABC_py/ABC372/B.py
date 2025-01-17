M = int(input())
A = []
i = 10
N = 0
while M != 0:
    if M / pow(3, i) >= 1:
        A.append(i)
        M -= pow(3, i)
        N += 1
    else:
        i -= 1
print(N)
for i in range(N):
    print(A[i], end = " ")