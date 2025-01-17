L ,R = input().split()
l_ans, r_ans = 1, 1
l_len, r_len = len(L), len(R)
l = int(L[0])
Lok = True
for i in range(1, l_len):
    if int(L[-1 * i]) < l:
        l_ans *= l - int(L[- 1 * i])
        Lok = False
    else:
        L[-1 * i - 1] = str(int(L[-1 * i - 1]) + 1)
        l_ans *= l
if Lok:
    l_ans = 0
l = (l + 1) * 10 ** l_len
r = int(R[0])
for i in range(1, len(R)):
    if int(R[i]) >= r:
        r_ans *= r - 1
    else:
        r_ans *= int(R[i])
r *= 10 ** r_len

if l > r:
    print(l_ans - r_ans)
    exit()
ans = 0
while r > l:
    L = list(str(l))
    l = int(L[0])
    for i in range(l):
        ans += i ** (len(L) - 1)
    l = (l + 1) * 10 ** l_len
print(ans + l_ans + r_ans)