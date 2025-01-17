N, M = map(int, input().split())
A = list(map(int, input().split()))


if sum(A) <= M:
    print("infinite")
    exit()

ok, ng = 0, max(A)

def disum(l):
    s = sum(min(l, a) for a in A)
    return s <= M     # bool型でreturn

# 二分探索

while ok + 1 < ng:
    mid = (ok + ng) // 2
    if disum(mid):
        ok = mid
    else:
        ng = mid

print(ok)
