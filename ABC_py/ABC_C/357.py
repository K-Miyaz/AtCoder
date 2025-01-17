N = int(input())
N3 = pow(3, N)
d = [["."] * N3 for _ in range(N3)]

def carpet(i, j, n):
    if n == 1:
        d[i][j] = "#"
    else:
        n = n // 3
        for k in range(3):
            for l in range(3):
                if k == 1 and l == 1:
                    continue
                carpet(i + n * k , j + n * l, n)

carpet(0, 0, N3)
for ans in d:
    print("".join(ans))
