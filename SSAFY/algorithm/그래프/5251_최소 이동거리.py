def dijk():
    D[0][0] = 0
    while len(U) < N:
        minv = E * 1000000
        for i in range(N):
            if i in U: continue
            if D[i][0] < minv:
                minv = D[i][0]
                curv = i
        U.append(curv)

        for i in range(N):
            if i in U: continue
            if Arr[curv][i] > 0:
                if D[i][0] > D[curv][0] + Arr[curv][i]:
                    D[i][0] =D[curv][0] + Arr[curv][i]


TC = int(input())
for tc in range(1, TC + 1):
    N, E = map(int, input().split())
    N = N + 1
    Arr = [[0] * N for _ in range(N)]
    for i in range(E):
        s1, s2, w = map(int, input().split())
        Arr[s1][s2] = w
    D = [[E*10000000] for _ in range(N)]
    U = []
    dijk()
    print(f'#{tc} {D[N-1][0]}')
'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
