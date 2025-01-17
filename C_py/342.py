def main():
    # N と S を入力
    N = int(input())  # N: 文字列の長さ
    S = input()  # S: 入力される文字列

    Q = int(input())  # Q: クエリ数

    # root[c] := 文字 c に対応する根
    # parent[i] := 頂点 i の親
    root = [None] * 26  # 文字 a~z の対応する根 (a -> 0, b -> 1, ..., z -> 25)
    parent = [None] * N  # 各頂点の親を格納

    # 最初に根を設定
    for i in range(N):
        c = ord(S[i]) - ord('a')  # 文字をインデックスに変換 (a -> 0, b -> 1, ...)
        if root[c] is not None:  # 既に根があれば
            parent[root[c]] = i  # その根の親を現在の i に設定
        root[c] = i  # 現在の i を文字 c の根として設定

    # クエリ処理
    for _ in range(Q):
        c, d = input().split()  # クエリ入力
        c = ord(c) - ord('a')  # 文字 c をインデックスに変換
        d = ord(d) - ord('a')  # 文字 d をインデックスに変換

        if c == d:  # c == d なら何もしない
            continue

        if root[c] is None:  # c の根がなければ何もしない
            continue

        if root[d] is None:  # d の根がなければ
            root[d] = root[c]  # c の根を d の根に設定
            continue

        # どちらも根があれば
        parent[root[c]] = root[d]  # c の根を d の根の子にする
        root[c] = None  # c の根はなくなる

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

if __name__ == "__main__":
    main()
