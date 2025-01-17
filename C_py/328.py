N, Q = map(int, input().split())
S = input()

sam_S = [0]
temp = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        temp += 1
    sam_S.append(temp)

for i in range(Q):
    l, r = map(int, input().split())
    print(sam_S[r - 1] - sam_S[l - 1])