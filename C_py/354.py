N = int(input())
num = set()
ans = []
AC = [[0] * 3 for _ in range(N + 1)]
for i in range(N):
    A, C = map(int, input().split())
    AC[i][0] = A
    AC[i][1] = C
    AC[i][2] = i + 1

# 強い順にソートし、コストが高いものをnumに追加
AC.sort(reverse=True, key=lambda x: x[0])
low_cost = AC[0][1]
for i in range(N):
    if low_cost < AC[i][1]:
        num.add(AC[i][2])
    else:
        low_cost = AC[i][1]

# コスト順にソートし、弱いものをnumに追加
AC.sort(key=lambda x: x[1])
str_A = AC[0][0]
for i in range(N):
    if str_A > AC[i][0]:
        num.add(AC[i][2])
    else:
        str_A = AC[i][0]

for i in range(1, N + 1):
    if i not in num:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))