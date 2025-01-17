N = int(input())
A = list(map(int, input().split()))
box = [A[0]]

for i in range(1, N):
    box.append(A[i])
    for j in range(len(box) - 1, 0, -1):
        if box[j] == box[j - 1]:
            a = box[j]
            box.pop(-1)
            box.pop(-1)
            box.append(a + 1)
        else:
            break

print(len(box))