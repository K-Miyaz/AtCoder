N = int(input())
n = 0
Repuit = [1] * 3
ans = 0
i_0 = 0
while N > n:
    minus_i = 0
    i_0 += 1
    for j in range(i_0):
         minus_i += j
    n_lit = n
    n += i_0 ** 2 - minus_i 
Repuit[0] = int("1" * i_0)

"""
print(i_0)
print(N - n_lit)
print(Repuit)
"""

i_1 = 0
for i in range(1, i_0 + 1):
    j = 0
    for j in range(1, i + 1):
        i_1 += 1
        if (N - n_lit) == i_1:
            break
    if (N - n_lit) == i_1:
        break

Repuit[1] = int("1" * (i))
Repuit[2] = int("1" * (j))
print(sum(Repuit))