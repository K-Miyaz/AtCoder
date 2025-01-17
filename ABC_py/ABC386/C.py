K = int(input())
S = input()
T = input()
ls = len(S)
lt = len(T)

if S == T:
    print("Yes")
    exit()
if ls == lt - 1:
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
    ans = False
    for i in range(ls):
        if S[i] == T[i]:
            continue
        else:
            if ans:
                ans = False
                break
            else:
                ans = True
    if ans:
        print("Yes")
    else:
        print("No")
elif ls == lt + 1:
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