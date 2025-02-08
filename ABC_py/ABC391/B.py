N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
T = []
for _ in range(M):
    T.append(input())

for i in range(N - M + 1):
    for j in range(N - M + 1):
        ST = True
        for k in range(M):
            for l in range(M):
                if S[i + k][j + l] == T[k][l]:
                    ST = True
                else:
                    ST = False
                    break
            if not ST:
                break
        if ST:
            print("{} {}".format(i + 1, j + 1))