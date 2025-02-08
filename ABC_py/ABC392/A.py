A = list(map(int, input().split()))

ans = False
for i in range(3):
    if A[i - 2] * A[i - 1] == A[i]:
        ans = True
if ans:
    print("Yes")
else:
    print("No")