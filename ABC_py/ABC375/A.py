N = int(input())
S = input()
ans = 0

for i in range(len(S) - 2):
    if S[i] == "#" and S[i+1] == "." and S[i+2] == "#":
        ans += 1
print(ans)