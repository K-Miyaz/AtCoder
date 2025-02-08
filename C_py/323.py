N, M = map(int, input().split())
A = list(map(int, input().split()))
S = []
for _ in range(N):
    S.append(input())

# AC:正解済み NAC:未正解
AC_score = [0] * N
NAC_score = [[0]] * N
for i in range(N):
    AC_score[i] = i + 1
    for j in range(M):
        if S[i][j] == "o":
            AC_score[i] += A[j]
        if S[i][j] == "x":
            NAC_score[i].append(A[j])

top_score = max(AC_score)
for i in range(N):
    if AC_score[i] == top_score:
        ans = 0
        print(ans)
        continue
    NAC = sorted(NAC_score[i], reverse=True)
    for j in range(len(NAC) - 1):
        AC_score[i] += NAC[j]
        if AC_score[i] >= top_score:
            ans = j + 1
            print(ans)
            break
