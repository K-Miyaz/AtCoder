N = int(input())
A = list(map(int, input().split()))
ans = 0

r = 1
l_list = [i for i in range(N - 1, -1, -1)]
while l_list:
    l = l_list.pop()
    while r < N:
        if A[l] * 2 <= A[r]:
            l_list.pop(r - l - 2 * ans)
            ans += 1
            r += 1
            break
        r += 1

print(ans)