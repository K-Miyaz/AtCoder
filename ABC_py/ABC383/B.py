H, W, D = map(int, input().split())
S = []
Floor = []
ans = [0] * 2 
for i in range(H):
    S.append(input())
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            Floor.append([i, j])

for i, j in Floor:
    now_ans = 0
    for i_ in range(i - D - 1, i + D):
        for j_ in range(j - D - 1, j + D):
            if 0 <= i_ < H and 0 <= j_ < W:
                if abs(i - i_) + abs(j - j_) <= D:
                    if S[i_][j_] == ".":
                        now_ans += 1
    ans.append(now_ans)
ans.sort(reverse=True)
print(ans[0] + ans[1])
