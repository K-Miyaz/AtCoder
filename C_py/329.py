from itertools import groupby

def run_length_encoding(S):
    return [(char, len(list(group))) for char, group in groupby(S)]

N = int(input())
S = input()
# アルファベットと0を辞書形式で対応付け
ans = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
result = run_length_encoding(S)

for i, j in result:
    temp = ans[i]
    ans[i] = max(j, temp)
print(sum(ans.values()))