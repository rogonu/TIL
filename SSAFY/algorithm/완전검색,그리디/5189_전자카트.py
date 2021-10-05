def solve(k):
    global minv

    if k == N:
        res[-1] = 0
        sumv = 0
        # sumV = 구해진 순열에 대한 배터리량 계산
        # 최소값을 구한다

        for i in range(N):

            st = res[i]
            ed = res[i+1]
            sumv += Arr[st][ed]
        if minv > sumv:
            minv = sumv
        return
    for i in range(N):
        if not visited[i]:
            res[k] = i
            visited[i] = True
            solve(k + 1)
            visited[i] = False

    #     방분 안한 경우:
    #         방문표시
    #         per(k+1)
    #         방문원복
    #
    # res[0] = 0
    # visited[0] = 방문표시
    # per(1)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    visited[0] = True
    minv = 999999999999999
    res = [-1] * (N + 1)
    res[0] = 0
    solve(1)
    print(f'#{tc} {minv}')
