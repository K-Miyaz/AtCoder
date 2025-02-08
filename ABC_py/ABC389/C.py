Q = int(input())

L = []
M = 0
c = 0
for _ in range(Q):
    query = input()
    if query[0] == "2":
        c += 1
        continue
    q_num, q_l = map(int, query.split(" "))
    if q_num == 1:
        if len(L) == 0:
            L.append(q_l)
        else:
            L.append(L[-1] + q_l)
    if q_num == 3:
        if q_l == 1:
            print(0)
            continue
        if c == 0:
            print(L[q_l - 2 + c])
        else:
            print(L[q_l - 2 + c] - L[c - 1])