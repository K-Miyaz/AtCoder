N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

PQ = []
for i in range(N):
    PQ.append([P[i], Q[i]])

PQ.sort(key=lambda x: x[1])
for i in range(N):
    looking = PQ[i][0] - 1
    print(Q[looking], end = " ")
