def solve(k, suc):
    global maxv
    if maxv >= suc:
        return
    if k == N:
        if suc > maxv:
            maxv = suc
        return

    for i in range(N):
        if not charged[i]:
            res[k] = i
            charged[i] = True
            solve(k+1, suc * P[k][i]/100)
            charged[i] = False

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    charged = [False] * N
    res = [-1] * N
    maxv = 0
    solve(0, 100)
    print('#{} {:.6f}'.format(tc,maxv))
