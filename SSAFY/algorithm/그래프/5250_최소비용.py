from collections import deque

def dijk():
    Q = deque()
    Q.append((0,0))
    D[0][0] = 0

    while Q:
        curx, cury = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newx = curx + dx
            newy = cury + dy
            if 0<= newx < N and 0 <= newy < N:
                # if Arr[newx][newy] > Arr[curx][cury]
                #     fuel = Arr[newx][newy] - Arr[curx][cury] + 1
                fuel = max(Arr[newx][newy] - Arr[curx][cury], 0) + 1
                if D[newx][newy] > D[curx][cury] + fuel:
                    D[newx][newy] = D[curx][cury] + fuel
                    Q.append((newx, newy))


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[N*N*1000] *N for _ in range(N)]
    U = []
    dijk()
    print(f'#{tc} {D[N-1][N-1]}')