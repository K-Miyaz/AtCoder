N = int(input())
N3 = pow(3, N)
d = [["."] * N3 for _ in range(N3)]

def carpet(i, j, n):
    if n == 1:
        d[i][j] = "#"
    else:
        n = n // 3
        for x in range(3):
            for y in range(3):
                if x % 3 == 1 and y % 3 == 1:
                    continue
                else:
                    carpet(x + 3 * i, y + 3 * j, n)

carpet(0, 0, N3)
for ans in d:
    print("".join(ans))