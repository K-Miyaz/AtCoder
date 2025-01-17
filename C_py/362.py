N = int(input())
LR = [map(int, input().split()) for _ in range(N)]
L, R = [list (i) for i in zip(*LR)]
l, r = sum(L), sum(R)

if l > 0 or r < 0:
    print("No")
    exit()

for i in range(N):
    if l < 0:
        diff = R[i] - L[i]
        if l + diff < 0:
            L[i] = R[i]
            l += diff
        else:
            L[i] += 0 - l
            break
    else:
        break

L = [str(i) for i in L]
print("Yes")
print(" ".join(L))