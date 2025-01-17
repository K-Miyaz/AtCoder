N = int(input())
S = input()
Q = int(input())

# root[c] := 文字 c に対する根
# parent[i] ;= 頂点 i の親

root = [None] * 26
parent = [None] * N

for i in range(N):
    c = ord(S[i]) - ord("a")
    if root[c] is not None:
        parent[root[c]] = i
    root[c] = i

for i in range(Q):
    c, d = map(str, input().split())
    c = ord(c) - ord("a")
    d = ord(d) - ord("a")

    if c == d:
        continue
    if root[c] is None:
        continue
    if root[d] is None:
        root[d], root[c] = root[c], root[d]
        continue
    
    parent[root[c]] = root[d]
    root[c] = None
# 結果を格納するためのリスト
result = [None] * N

for c in range(26):
    if root[c] is not None:  # root[c] が存在する場合
        result[root[c]] = chr(c + ord('a'))  # 文字列の対応を設定 (a -> 0, b -> 1, ...)

# 結果を計算する
for i in range(N):
    if result[i] is None:  # まだ値が決まっていない場合
        index = []
        now = i
        while result[now] is None:  # 値が決まるまで親をたどる
            index.append(now)
            now = parent[now]
        # 親をたどった順番で結果を設定
        for j in index:
            result[j] = result[now]

    # 結果を出力
    print(result[i], end="")

# 改行を出力
print()
