N, M = map(int,input().split())
xy = [map(str,input().split()) for i in range(M)]
x, y = [list (i) for i in zip(*xy)]
n = [0] * N
for i in range(M):
    X = int(x[i]) - 1
    if n[X] == 0 and y[i] == "M":
        print("Yes")
        n[X] = 1
    else:
        print("No")