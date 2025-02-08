N = int(input())
K = []
A = []
ans = 0
for i in range(N):
    numbers = list(map(int, input().split()))
    K.append(numbers[0])
    A.append(sorted(numbers[1:]))
    
for i in range(N):
    for j in range(i + 1, N):
        # k : A[i]の変数 l : A[j]の変数
        k = 0; l = 0
        # k_same : kを変更したとき同じA[i]が同じ場合のカウント
        k_same = 1; l_same = 1
        same_num = 0
        while (k < K[i] and l < K[j]):
            if A[i][k] == A[j][l]:
                if k < K[i] - 1:
                    if A[i][k] == A[i][k + 1]:
                        k += 1
                        k_same += 1
                        continue
                if l < K[j] - 1:
                    if A[j][l] == A[j][l + 1]:
                        l += 1
                        l_same += 1
                        continue
                same_num += k_same * l_same
                k += 1; l += 1
                k_same = 1; l_same = 1
            elif A[i][k] > A[j][l]:
                l += 1
            else:
                k += 1
        ans = max(ans, same_num / (K[i] * K[j]))

print(ans)