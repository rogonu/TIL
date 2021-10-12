di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
def find(i,j):
    t = 0
    for d in range(4):
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i <N and 0 <= new_j < N:
            if rooms[new_i][new_j] == rooms[i][j] + 1 :
                t = find(new_i, new_j)
    return t + 1

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    maxc = 0
    maxv = 0
    for i in range(N):
        for j in range(N):
            cnt = find(i,j)
            if cnt > maxc:
                maxc = cnt
                maxv = rooms[i][j]
            elif cnt == maxc and rooms[i][j] < maxv:
                maxv = rooms[i][j]
    print(f'#{tc} {maxv} {maxc}')
