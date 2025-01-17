S = input()
A = []
j = 0
for i in range(1, len(S)):
    if S[i] == "|":
        A.append(i - j - 1)
        j = i
for i in A:
    print(i, end=" ")