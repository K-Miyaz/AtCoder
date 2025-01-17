S = input()
T = input()
X = []
for i in range(len(S)):
    if S[i] > T[i]:
        S = S[:i] + T[i] + S[i+1:]
        X.append(S)
for j in range(1,len(S) + 1):
    i = j * -1
    if S[i] != T[i]:
        J = len(S) + i
        S = S[:J] + T[J] + S[J+1:]
        X.append(S)
print(len(X))
for i in range(len(X)):
    print(X[i])