N = int(input())
LR = [map(int, input().split()) for _ in range(N)]
L, R = [list (i) for i in zip(*LR)]
X = []
ans = False

for i in range(N):
    X.append(L[i])
for i in range(N):
    if sum(X) == 0:
        ans = True
        break
    while L[i] < R[i]:
        X[i] = (L[i] + R[i]) // 2
        # print("L = {}, R = {}".format(L[i], R[i]))
        if sum(X) < 0:
            if L[i] == X[i]:
                L[i] = X[i] + 1
            else:
                L[i] = X[i]
        elif sum(X) > 0:
            if R[i] == X[i]:
                R[i] = X[i] - 1
            else:
                R[i] = X[i]
        else:
            ans = True
            break
    if ans:
        break
X = [str(i) for i in X]
if ans:
    print("Yes")
    print(" ".join(X))
else:
    print("No")