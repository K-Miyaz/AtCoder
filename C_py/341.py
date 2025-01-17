H, W, N = map(int,input().split())
T = list(input())
S = []
ans = 0
for _ in range(H):
    S.append(list(input()))

def move(i, j, s):
    if s == "L":
        return i, j - 1
    elif s == "R":
        return i, j + 1
    elif s == "U":
        return i - 1, j
    elif s == "D":
        return i + 1, j
    else:
        print("error")

for i in range(1, H - 1):
    for j in range(1, W - 1):
        seaflag = True
        if S[i][j] == "#":
            seaflag = False
        now_i = i
        now_j = j
        for t in T:
            now_i, now_j = move(now_i, now_j, t)
            if S[now_i][now_j] == "#":
                seaflag = False
                break
        if seaflag:
            ans += 1

print(ans)