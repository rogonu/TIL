

def dfs(v):
    di = [0, 0, 1, -1]  # 우좌하상
    dj = [1, -1, 0, 0]
    que = []
    # visited = [[0] * N for _ in range(N)]   visited 를 새로 만들지 않고 지나간 길이면 +1 하느 식으로 바꾼다
    que.append(v)
    Arr[v[0]][v[1]] = 1
    while que:
        v = que.pop(0)
        for d in range(4):
            if 0 <= v[0] + di[d] < N and 0 <= v[1] + dj[d] < N and (v[0] + di[d], v[1] + dj[d]) == E:
                return Arr[v[0]][v[1]] - 1
            if 0 <= v[0] + di[d] < N and 0 <= v[1] + dj[d] < N and not Arr[v[0] + di[d]][v[1] + dj[d]]:
                que.append((v[0] + di[d], v[1] + dj[d]))
                Arr[v[0] + di[d]][v[1] + dj[d]] = Arr[v[0]][v[1]] + 1
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input())) for _ in range(N)]
    S = (0, 0)
    E = (0, 0)
    for i in range(N):
        for j in range(N):
            if Arr[i][j] == 2:
                S = (i, j)
            elif Arr[i][j] == 3:
                E = (i, j)
    print('#{} {}'.format(tc, dfs(S)))
