N, K = map(int, input().split())
S = list(input())
A = []
j = 0

for i in range(N):
    if S[i] == "0":
        if i > 0 and S[i - 1] == "1":
            A.append([j, i - j])
    elif i > 0 and S[i - 1] != "1":
        j = i
    if i == N - 1 and S[-1] == "1":
        A.append([j, i - j + 1])

A[K - 2][1] += A[K - 1][1]
A.pop(K - 1)
A.append([10 ** 6, 0])

j = 0
i = 0
while i < N:
    if A[j][0] > i:
        print("0", end="")
        i += 1
    else:
        for k in range(A[j][1]):
            print("1", end= "")
            i += 1
        j += 1
