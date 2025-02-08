H, W = map(int, input().split())
S = []
A = []
T = []
for i in range(H):
    S.append(input())
    T.append(list(S[i]))
ans = 0

def check(x, i, y, j):
    if x + i < 0 or y + j < 0:
        return False
    if x + i >= H or y + j >= W:
        return False
    return True
c = 0
for x in range(H):
    for y in range(W):
        if S[x][y] == "#":
            c += 1
            if T[x][y] == "#":
                temp = -1
            else:
                temp = 0
            for i in range(-1, 1 + 1):
                for j in range(-1, 1 + 1):
                    if check(x, i, y, j):
                        if T[x + i][y + j] == "#":
                            T[x + i][y + j] = "@"
                            temp += 1
            A.append(temp)
print(T)
print(A)
print(c - sum(A))