S = []
take = [[0] * 8 for _ in range(8)]
ans = 0
for _ in range(8):
    S.append(input())

for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            for k in range(8):
                take[i][k] = 1
            for k in range(8):
                take[k][j] = 1
for i in range(8):
    for j in range(8):
        if take[i][j] == 0:
            ans += 1

print(ans)