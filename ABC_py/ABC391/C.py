N, Q = map(int, input().split())
# その巣に何匹の鳥がいるかを保存
nest = [1] * N
# その鳩が今どこにいるかを保存
bird = [i for i in range(N)] 
ans = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 入力が1からなので0からに変更
        query[1] -= 1
        query[2] -= 1

        # 鳩pが移動前の処理
        # 鳩Pのいる位置をbird_nowに
        bird_now = bird[query[1]]
        #　鳩pがいる巣が2匹の場合複数の巣の数が減る為1減らす
        if nest[bird_now] == 2:
            ans -= 1
        # 鳩pがいる巣にいる鳩の数を減らす
        nest[bird_now] -= 1

        # 鳩pが移動後の処理
        # 鳩pがいる位置を変更
        bird[query[1]] = query[2]
        # 鳩pがいる巣が1匹の場合複数の巣の数が増える為1増やす
        if nest[query[2]] == 1:
            ans += 1
        # 鳩pがいる巣にいる鳩の数を増やす
        nest[query[2]] += 1
    if query[0] == 2:
        print(ans)