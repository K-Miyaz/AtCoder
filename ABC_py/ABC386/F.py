K = int(input())
S = input()
T = input()
ls = len(S)
lt = len(T)

if S == T:
    print("Yes")
    exit()
if lt - K <= ls < lt:
    j = 0
    for i in range(lt):
        if j == ls:
            break
        ns = S[j]
        nt = T[i]
        if ns == nt:
            j += 1
    if j == ls:
        print("Yes")
    else:
        print("No")
elif ls == lt:
    ans = 0
    for i in range(ls):
        if S[i] == T[i]:
            continue
        else:
            ans += 1
            if ans > K:
                break
    if ans <= K:
        print("Yes")
    else:
        print("No")
elif lt < ls <= lt + K:
    j = 0
    for i in range(ls):
        if j == lt:
            break
        ns = S[i]
        nt = T[j]
        if ns == nt:
            j += 1
    if j == lt:
        print("Yes")
    else:
        print("No")
else:
    print("No")