S = input()
ok = True
Sset = set()
if len(S) % 2 == 1:
    ok = False

for i in range(0, len(S), 2):
    if ok == False:
        break
    if S[i] != S[i + 1]:
        ok = False
    if S[i] in Sset:
        ok = False
    else:
        Sset.add(S[i])
if ok:
    print("Yes")
else:
    print("No")