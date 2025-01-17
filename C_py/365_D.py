N = int(input())
S = input()
dp = [[0] * (N + 1) for _ in range(2)]
f_inf_minus = -10 ** 9

# 動的計画法

def drow(A):
    if A == "R":
        return 1
    elif A == "P":
        return 2
    else:
        return 3

def win(A):
    if A == "R":
        return 2
    elif A == "P":
        return 3
    else:
        return 1

# 前に出した手
db = drow(S[0]); wb = win(S[0])
for i in range(N):
    # これから出す手
    da = drow(S[i])
    wa = win(S[i])
    # i回目にじゃんけんに勝った時の最大勝利数
    wk, dk = 1, 1
    # 連続で同じ手を出した場合の処理
    if wb == wa:
        wk = f_inf_minus
    elif db == wa:
        dk = f_inf_minus
    dp[0][i + 1] = max(dp[0][i] + wk, dp[1][i] + dk)

    # i回目にじゃんけんに分けた時の最大勝利数
    wk, dk = 0, 0
    # 連続で同じ手を出した場合の処理
    if wb == da:
        wk = f_inf_minus
    elif db == da:
        dk = f_inf_minus
    dp[1][i + 1] = max(dp[0][i] + wk, dp[1][i] + dk)
    # 出した手を変更
    wb = wa; db = da
    # print("{} {}".format(dp[0][i + 1], dp[1][i + 1]))

print(max(dp[0][N], dp[1][N]))