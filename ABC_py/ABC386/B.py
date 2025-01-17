S = input()
ans = 0
zero = False
for i in range(len(S)):
    if S[i] == "0":
        if zero:
            zero = False
            continue
        else:
            zero = True
            ans += 1
    else:
        zero = False
        ans += 1

print(ans)