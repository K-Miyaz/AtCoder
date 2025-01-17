N, Q = map(int, input().split())
dragon = [[i, 0] for i in range(N, 0, -1)]

# 指定された方向に移動
def move(C, i, j):
    if C == "R":
        dragon.append([i + 1, j])
    elif C == "L":
        dragon.append([i - 1, j])
    elif C == "U":
        dragon.append([i, j + 1])
    elif C == "D":
        dragon.append([i, j - 1])

for i in range(Q):
    query_num, query_C = input().split()

    # 移動する場合
    if query_num == "1":
        head_x, head_y =dragon[-1]
        move(query_C, head_x, head_y)
    # 指定位置の出力
    else:
        C = int(query_C)
        if 0 <= C:  # 範囲チェック
            print(*dragon[-int(C)])
        else:
            print("Error: 指定されたセグメントが存在しません")