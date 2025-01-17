N = input()
d = len(N)
ans = 20

for num in range(2 ** d):
    tmp_ans = d
    tmp_N = [0] * d
    per3 = 0
    for i in range(d):
        if ((num >> i) & 1):
            tmp_N[i] = int(N[i])
            tmp_ans -= 1
    for i in range(d):
        per3 += tmp_N[i]
    if per3 == 0:
        continue
    if per3 % 3 == 0 and tmp_ans < ans:
        ans = tmp_ans
if ans == 20:
    print(-1)
else:
    print(ans)
