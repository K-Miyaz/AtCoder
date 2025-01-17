N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
ans = 0
ans_i = 0
no_ans = 0
no_ans_i = 0
for i in range(N):
    if C[i] == T:
        if R[i] > ans:
            ans = R[i]
            ans_i = i
    elif C[i] == C[0]:
        if R[i] > no_ans:
            no_ans = R[i]
            no_ans_i = i

if ans > 0:
    print(ans_i + 1)
else:
    print(no_ans_i + 1)