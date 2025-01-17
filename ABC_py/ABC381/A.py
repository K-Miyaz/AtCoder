N = int(input())
S = input()

if N % 2 == 0:
    print("No")
    exit()
ok = True
for i in range(N):
    if i < (N // 2):
        if S[i] != "1":
            ok = False
    elif i == (N // 2):
        if S[i] != "/":
            ok = False
    else:
        if S[i] != "2":
            ok = False

if ok:
    print("Yes")
else:
    print("No")