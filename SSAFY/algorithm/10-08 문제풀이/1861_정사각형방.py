di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
def find(x):


    for i in range(N):
        for j in range(N):
            res[i][j]
            for k in range(4):
                if 
                res[i + di[k]][j + dj[k]]

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    res = [[0] * N for _ in range(N)]
