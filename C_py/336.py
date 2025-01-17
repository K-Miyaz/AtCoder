N = int(input())
N -= 1
ans = []

i = 0
while True:
    ans.append(10 ** i * (N % 5) * 2)
    if N // 5 < 1:
        break
    N = N // 5
    i += 1
print(sum(ans))