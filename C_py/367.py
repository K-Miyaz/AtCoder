N, K = map(int, input().split())
R = list(map(int, input().split()))
ans_list = []

def Rn(n):
    for i in range(1, R[n] + 1):
        ans_list.append(i)
        if n < N - 1:
            Rn(n + 1)
        else:
            if sum(ans_list) % K == 0:
                for j in ans_list:
                    print(j, end= " ")
                print()
        ans_list.pop(-1)

Rn(0)