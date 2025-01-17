N, M = map(int, input().split())
A = list(map(int, input().split()))
a = [0]
ans = 10 ** 9

ave = M // N
remainder = -1* (M % N)
min_cost = 0

if M >= sum(A):
    print("infinite")
    exit()

for i in range(N):
    a_app = A[i] - ave
    if a_app <= 0:
        remainder += a_app
        if ans < A[i]:
            ans = A[i]
    if a_app > 0:
        a.append(a_app)
a.sort()
for i in range(1, len(a)):
    if (remainder * -1) > ((a[i] - a[i - 1]) * (len(a) - i)):
        remainder += (a[i] - a[i - 1]) * (len(a) - i)
    elif (remainder * -1) == ((a[i] - a[i - 1]) * (len(a) - i)):
        ans = a[i] + ave
        break
    else:
        ans = a[i - 1] + ave
        break

print(ans)