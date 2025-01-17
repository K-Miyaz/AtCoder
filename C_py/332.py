N, M = map(int, input().split())
S = input()
m = M
ans = 0
temp = 0
for i in range(N):
    # 食事に行く
    if S[i] == "1":
        # 無地T有
        if m > 0:
            m -= 1
        # 無地T無、ロゴT有
        elif temp > 0:
            temp -= 1
        # 無地T無、ロゴT無
        else:
            ans += 1
    #　競プロに行く
    if S[i] == "2":
        # ロゴT有
        if temp > 0:
            temp -= 1
        # ロゴT無
        else:
            ans += 1
    # 洗濯
    if S[i] == "0":
        m = M
        temp = ans
print(ans)