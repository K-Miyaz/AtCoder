N = int(input())
ans = 0

nico = [25, 2525, 252525, 25252525]
for i in nico:
    ans += N // i
print(ans)