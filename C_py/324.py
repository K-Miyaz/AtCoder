N, T = input().split()
ans = []

def check_diff_len(s, t):
    ok = True
    j = 0
    for i in range(len(t)):
        if j == len(t) - 1:
            break
        if s[j] == t[i]:
            j += 1
        else:
            if ok:
                ok = False
            else:
                return False
    return True

def check_diff_str(s, t):
    ok = True
    for i in range(len(t)):
        if S[i] != t[i]:
            if ok:
                ok = False
            else:
                return False
    return True

for i in range(int(N)):
    S = input()
    if not(len(T) - 1 <= len(S) <= len(T) + 1):
        continue
    if S == T:
        ans.append(i + 1)
        continue
    if len(S) < len(T) and check_diff_len(S, T):
        ans.append(i + 1)
        continue
    if len(S) == len(T) and check_diff_str(S, T):
        ans.append(i + 1)
        continue
    if len(S) > len(T) and check_diff_len(T, S):
        ans.append(i + 1)
        continue

print(len(ans))
for i in ans:
    print(i, end=" ")