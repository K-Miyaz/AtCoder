N, M = 9, 3
A = []
check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check = False
for i in range(9):
    A.append(list(map(int, input().split())))

# 各列に1~9がちょうど1個ずつか
for i in range(N):
    A_line = []
    check = True
    for j in range(N):
        A_line.append(A[i][j])
    A_line.sort()
    if check_list == A_line:
        check = False
    if check:
        print("No")
        exit()

# 各行に1~9がちょうど1個ずつか
for i in range(N):
    A_line = []
    check = True
    for j in range(N):
        A_line.append(A[j][i])
    A_line.sort()
    if check_list == A_line:
        check = False
    if check:
        print("No")
        exit()

# 各3*3に1~9がちょうど1個ずつか
for i in range(M):
    for j in range(M):
        A_line = []
        check = True
        for k in range(M):
            for l in range(M):
                A_line.append(A[3 * i + k][3 * j + l])
        A_line.sort()
        if check_list == A_line:
            check = False
        if check:
            print("No")
            exit()
print("Yes")