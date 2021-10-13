def dfs(x):
    global res
    cnt = 0
    st = []
    st.append(x)

    while st:
        v = st.pop()
        if not visited[v]:
            cnt += 1
            visited[v] = True
            if cnt > res:
                res = cnt
            for w in Arr[v]:
                if not visited[w]:
                    st.append(w)



TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Arr = [[] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        Arr[x].append(y)
        Arr[y].append(x)
    visited = [False] * (N+1)
    res = 0
    for j in range(1,N+1):
        dfs(j)
    print(f'#{tc} {res}')
