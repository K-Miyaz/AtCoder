from functools import cache

N = int(input())

@cache
def f(x):
    if x == 1:
        return 0
    else:
        return x + f(x // 2) + f(x - (x // 2))
ans = f(N)
print(ans)