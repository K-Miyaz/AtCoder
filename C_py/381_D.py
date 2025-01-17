from collections import deque
N = int(input())
A = input().split()
Aset = set()
ans = 0
now = 0
i = 1
ilist = deque()
while i < N:
    if A[i] in Aset:
        if ans < now:
            ans = now
        Aset = set()
        now = 0
        i = ilist.popleft()
        continue
    else:
        if A[i] == A[i - 1]:
            Aset.add(A[i])
            now += 2
            i += 2
            ilist.append(i)
        else:
            if ans < now:
                ans = now
            now = 0
            Aset = set()
            ilist = deque()
            i += 1

if ans < now:
    ans = now
print(ans)