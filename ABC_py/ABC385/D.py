N, M, Sx, Sy = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
T = set()

def move(t, x, y, C):
    if t == "U":
        return x, y + C
    if t == "D":
        return x, y - C
    if t == "L":
        return x - C, y
    if t == "R":
        return x + C, y

for i in range(M):
    D, c = input().split()
    C = int(c)
    next_x, next_y = move(D, Sx, Sy, C)
    if next_x == Sx:
        T.add((next_x, Sy + i) for i in range(1, C + 1))
    if next_y == Sy:
        T.add((Sx + i, Sy) for i in range(1, c + 1))
print("{} {} {}".format(Sx, Sy, len(T)))