N = int(input())
A = input().split()
Aset = set()
ans = 0
now = 0
i = 1
while i < N:
    if A[i] in Aset:
        if ans < now:
            ans = now
        Aset = set()
        i += 1
        now = 0
        continue
    else:
        if A[i] == A[i - 1]:
            Aset.add(A[i])
            now += 2
            i += 2
        else:
            if ans < now:
                ans = now
            Aset = set()
            i += 1
            now = 0

if ans < now:
    ans = now
print(ans)