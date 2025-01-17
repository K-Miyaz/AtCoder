N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

ans = 0
j = 0
for i in range(N):
    if A[i] <= B[j]:
        j += 1
        if j == len(B):
            break
    else:
        ans += A[i]
        if ans > A[i]:
            ans = -1
            break
if ans == 0:
    ans = A[-1]
print(ans)