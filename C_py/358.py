N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 10
for i in range(2 ** N):
    pa_ans = 0
    bag = ["x"] * M
    for j in range(N):
        if ((i >> j) & 1):
            pa_ans += 1
            for k in range(M):
                # print("{} {}".format(S[j][k], k), end = "  ")
                if S[j][k] == "o":
                    bag[k] = "o"
    bag_count = bag.count("o")
    if bag_count == M and ans > pa_ans:
        ans = pa_ans

print(ans)
