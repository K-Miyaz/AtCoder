N = int(input())
A = list(map(int, input().split()))
B = []

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid][0] == value:
            # 中央の値と一致した場合は位置を返す
            return data[mid][1] + 1, left
        elif data[mid][0] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1, left            # 見つからなかった場合

for i in range(N):
    ans, left = binary_search(B, A[i])
    if ans == -1:
        B.insert(left, A[i])
    print(ans, end=" ")