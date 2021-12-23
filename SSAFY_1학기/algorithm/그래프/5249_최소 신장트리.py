def prim():
    s = 0
    D[s][0] = 0

    while len(U) <= N:

        minV = N * w
        for i in range(N + 1):
            if i in U: continue
            if D[i][0] < minV:
                minV = D[i][0]
                curV = i

        U.append(curV)


        for j in range(N+1):
            if j in U: continue
            if G[curV][j] > 0:
                if D[j][0] > G[curV][j]:
                    D[j][0] = G[curV][j]

TC = int(input())
for tc in range(1, TC + 1):
    N, E = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w


    D = [[N*w] for _ in range(N+1)]
    U = []
    prim()
    sum = 0
    for i in range(N+1):
        sum += D[i][0]

    print(f'#{tc} {sum}')