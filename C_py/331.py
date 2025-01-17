N = int(input())
A_ = list(map(int, input().split()))
i_ = [i for i in range(N)]
A = [[a, b] for a, b in zip(A_, i_)]
B = [0]

A.sort(reverse = True, key = lambda x: x[0])
temp1 = 0   # 合計の値
temp2 = 0   # 前と同じ値が続いた場合の合計
for i in range(1, N):
    if A[i - 1][0] > A[i][0]:
        temp1 += A[i - 1][0]
        B.append(temp1)
        temp2 = temp1
    else:
        temp1 += A[i - 1][0]
        B.append(temp2)
for i in range(N):
    A[i][0] = B[i]
A.sort(key = lambda x: x[1])
for i in range(N):
    print(A[i][0])