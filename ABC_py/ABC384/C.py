A_ = list(map(int, input().split()))
N = len(A_)
i_ = [i for i in range(N)]
A = [[a, b] for a, b in zip(A_, i_)]

def number_to_char(number):
    # 数字を対応するアルファベットに変換
    return chr(number + ord('A'))

def numbers_to_string(numbers):
    return ''.join([number_to_char(n) for n in numbers])

B = []
for i in range(2 ** N):
    temp = 0
    temp_num = []
    for j in range(N):
        if ((i >> j) & 1):
            temp += A[j][0]
            temp_num.append(A[j][1])
    
    B.append([temp, numbers_to_string(temp_num)])

B.sort(reverse=True)
ans = []
temp = 0
temp_num = []
for i in range(len(B)):
    if temp != B[i][0]:
        temp = B[i][0]
        temp_num.sort()
        for j in range(len(temp_num)):
            print(temp_num[j])
        temp_num = [B[i][1]]
    else:
        temp_num.append(B[i][1])
