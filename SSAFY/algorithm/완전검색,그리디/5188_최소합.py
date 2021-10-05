import sys
sys.stdin = open('input.txt', 'r')

def solve(curx, cury, sumv):
    global minv
    if curx == N - 1 and cury == N - 1:
        if minv > sumv:
            minv = sumv
            return


    if curx + 1 < N:
        solve(curx + 1, cury, sumv + Arr[curx+1][cury])
    if cury + 1 < N:
        solve(curx, cury + 1, sumv + Arr[curx][cury + 1])
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    minv = N * N * 10
    solve(0, 0, Arr[0][0])

    print(f'#{tc} {minv}')


