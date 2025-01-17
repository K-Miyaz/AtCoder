
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
box = [[0]  for _ in range(N)]
ans = 0

for i in range(N):
    box[A[i] - 1].append(W[i])

for i in range(N):
    box[i] = sorted(box[i])
    # print(box[i])
    for j in range(len(box[i]) - 1):
        # print(box[i][j])
        ans += box[i][j]
print(ans)
