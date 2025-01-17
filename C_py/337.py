N = int(input())
A_ = list(map(int, input().split()))
i_ = [i for i in range(1, N + 1)]
A = [[a, b] for a, b in zip(A_, i_)]
ans = []

A.sort(key=lambda x: x[0])
ans.append(A[0][1])
A.pop(0)

for i in range(1, N):
    Ai = ans[-1]
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid][0] == Ai:
            ans.append(A[mid][1])
            break
        if A[mid][0] < Ai:
            left = mid
        else:
            right = mid

for i in range(N):
    print(ans[i], end= " ")