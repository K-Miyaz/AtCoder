N = int(input())
H = list(map(int, input().split()))
ans = 1
H_list = set()
for i in range(N):
    H_list.add(H[i])

for t in H_list:
    A = []
    for i in range(N):
        if H[i] == t:
            A.append(i)
    for i in A:
        for j in range(A[-1] - i):
            temp = 0
            n = 0
            while (i + n * j) in A:
                temp += 1
                n += 1
            ans = max(ans, temp)

print(ans)