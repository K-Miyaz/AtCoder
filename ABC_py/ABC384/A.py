n, c, c2 = input().split()
S = input()
N = int(n)
for i in range(N):
    if S[i] != c:
        print(c2, end="")
    else:
        print(c,end="")
