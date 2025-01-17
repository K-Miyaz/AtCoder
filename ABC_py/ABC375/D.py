S = input()
A = [S[0]]
a = [[0]]
ans = 0
for i in range(len(S)):
    new_word = True
    for j in range(len(A)):
        if A[j] == S[i]:
            new_word = False
            a[j].append(i)
        if new_word == True and j == (len(A) - 1):
            A.append(S[i])
            a.append([0])
for i in range(len(A)):
    for j in range(len(a[i])-1):
        for k in range(j + 1, len(a[i])):
            ans += a[k] - a[j] - 1
print(ans)