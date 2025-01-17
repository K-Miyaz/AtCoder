N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
A.append(0)
A.sort()
for i in range(1, N + 1):
    if A[i] > K:
        break
    if i == N:
        i += 1
        break
    elif A[i] == A[i - 1]:
        continue
    else:
        ans += int((A[i] + A[i - 1]) / 2 * (A[i] - A[i - 1] - 1))
ans += int(((K + 1) + A[i - 1]) / 2 * ((K + 1) - A[i - 1] - 1))
print(int(ans))