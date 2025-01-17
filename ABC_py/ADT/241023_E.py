S = input()
T = input()
j = 0

for i in range(len(S)):
    if S[i].upper() == T[j]:
        j += 1
    if j == 3:
        break
if j == 3:
    print("Yes")
elif j == 2 and T[2] == "X":
    print("Yes")
else:
    print("No")