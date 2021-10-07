def solve(k, sumv):
    global minv
    if sumv > minv:
        return
    if k == N:
        sumv = 0
        for i in range(N):
            f = res[i]
            sumv += V[i][f]
        if minv > sumv:
            minv = sumv
        return
    for i in range(N):
        if not used[i]:
            res[k] = i
            used[i] = True
            solve(k+1, sumv + V[k][i])
            used[i] = False


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    res = [-1] * N
    minv = 100* N
    solve(0,0)
    print(f'#{tc} {minv}')