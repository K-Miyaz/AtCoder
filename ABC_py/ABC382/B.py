N, D = map(int, input().split())
S = list(input())
j = -1
for i in range(D):
    while S[j] != "@":
        j -= 1
    S[j] = "."
print("".join(S))