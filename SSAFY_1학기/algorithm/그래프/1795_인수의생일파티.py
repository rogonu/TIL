def dijkstra(s,D,adj):
    U = []
    D[s] = 0
    while len(U) < N + 1:
        minV = 99999999999
        for i in range(N + 1):
            if i in U: continue
            if D[i] <  minV:
                minV = D[i]
                curv = i
        U.append(curv)

        for i in range(N + 1):
            if i in U: continue
            if D[i] > D[curv] + adj[curv][i]:
                D[i] = D[curv] + adj[curv][i]


TC = int(input())
for tc in range(1, TC + 1):
    N, M ,X = map(int, input().split()) # N: 사람수 M: 간선수 X : 인수집
    adj1 = [[99999999999]* (N+1) for _ in range(N+1)]
    adj2 = [[99999999999] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())  # c:가중치
        adj1[x][y] = c
        adj2[y][x] = c
    D1 = [99999999999] * (N + 1)
    D2 = [99999999999] * (N + 1)
    # 다익스트라 호출
    dijkstra(X,D1,adj1)
    dijkstra(X,D2,adj2)
    max_value = 0
    for i in range(1, N + 1):
        if D1[i] + D2[i] > max_value:
            max_value = D1[i] + D2[i]
    print(adj1)
    print(adj2)
    print(D1)
    print(D2)
    print(f'#{tc} {max_value}')