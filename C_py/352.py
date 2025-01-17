N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]
max_i = 0
for i in range(N):
    max_i = max(max_i, B[i] - A[i])
ans = sum(A) + max_i
print(ans)