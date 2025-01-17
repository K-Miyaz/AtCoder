H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
T = list(input())
C = set()

def move(t, x, y):
    if t == "U":
        return x - 1, y
    if t == "D":
        return x + 1, y
    if t == "L":
        return x, y - 1
    if t == "R":
        return x, y + 1
    
X, Y = X - 1, Y - 1

for i in range(len(T)):
    next_X, next_Y = move(T[i], X, Y)
    if S[next_X][next_Y] == "@":
        C.add((next_X, next_Y))
        X, Y = next_X, next_Y
    elif S[next_X][next_Y] == ".":
        X, Y = next_X, next_Y
X += 1
Y += 1
print("{} {} {}".format(X, Y, len(C)))