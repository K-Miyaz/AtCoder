N = int(input())
A = list(map(int, input().split()))

ans = 0
A.sort()
for i in A:
    if ans == int(i):
        ans += 1
    elif ans < i:
        break
print(ans)