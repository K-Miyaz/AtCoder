A = list(map(int, input().split()))
N = 3
ok = False
for i in range(N):
    if A[i] + A[i - 1] == A[i - 2]:
        ok = True
        break
    elif A[i] == A[i - 1]:
        ok = True

if ok:
    print("Yes")
else:
    print("No")