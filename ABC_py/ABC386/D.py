N, M = map(int, input().split())
B_row = [-1] * N
B_column = [-1] * N
W_row = [N - 1] * N
W_column = [N - 1] * N
ans = True
for _ in range(M):
    x, y, C = map(str, input().split())
    X, Y = int(x), int(y)
    if C == "B":
        B_row[X - 1] = max(B_row[X - 1], Y - 1)
        B_column[Y - 1] = max(B_column[Y - 1], X - 1)
    else:
        W_row[X - 1] = min(W_row[X - 1], Y - 1)
        W_column[Y - 1] = min(W_column[Y - 1], X - 1)
    if B_row[X - 1] > W_row[X - 1]:
        ans = False
        break
    if B_column[Y - 1] > W_column[Y - 1]:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")