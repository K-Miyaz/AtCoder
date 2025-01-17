N = int(input())
T = input()

def GoS(x, y, R):
    if R % 4 == 0:
        return x + 1, y
    elif R % 4 == 1:
        return x, y - 1
    elif R % 4 == 2:
        return x - 1, y
    else:
        return x, y + 1

x, y = 0, 0
Rcount = 0
for i in range(N):
    if T[i] == "S":
        x, y = GoS(x, y, Rcount)
    else:
        Rcount += 1

print("{} {}".format(x, y))