import math

N = int(input())

n = int(math.pow(N, 1/3)) + 1
for i in range(n, 0, -1):
    ok = True
    if pow(i, 3) > N:
        ok = False
    ans = list(str(pow(i, 3)))
    if ans != ans[::-1]:
        ok = False
    if ok:
        print("".join(ans))
        exit()