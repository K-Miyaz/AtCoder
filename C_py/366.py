Q = int(input())
M = 10 ** 6 + 1
c = [0] * M
kinds = 0

for _ in range(Q):
    s = input()
    if s[0] == "1":
        y, x = map(int, s.split())
        if c[x] == 0:
            kinds += 1
        c[x] += 1
    elif s[0] == "2":
        y, x = map(int, s.split())
        if c[x] == 1:
            kinds -= 1
        c[x] -= 1
    else:
        print(kinds)
