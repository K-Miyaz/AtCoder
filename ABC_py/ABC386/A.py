A = list(map(int, input().split()))
B = A[0]
b = 0
c = 0
for i in A:
    if B != i:
        C = i
        c += 1
if c > 0:
    c = 0
else:
    print("No")
    exit()
for i in A:
    if B == i:
        b += 1
    if C == i:
        c += 1

if (b == 2 and c == 2) or (b == 3 and c == 1) or (c == 3 and b == 1):
    print("Yes")
else:
    print("No")
