N = int(input())
S = input()
T = []
max = 1
for i in range(1, N):
    if S[i] == "/":
        T.append(i)
for i in T:
    now_max = 1
    j = 1
    while i + j < N:
        if i - j < 0:
            break
        if S[i - j] == "1" and S[i + j] == "2":
            now_max += 2
            j += 1
        else:
            break
    if now_max > max:
        max = now_max
print(max)