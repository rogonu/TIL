# def dfs(x, cnt):
#     global res
#     if cnt > res:
#         res = cnt
#
#     for k in Arr[x]:
#         if not visited[k]:
#             visited[x] = True
#             dfs(k,cnt + 1)
#             visited[k] = False
#
# TC = int(input())
# for tc in range(1, TC + 1):
#     N, M = map(int, input().split())
#     Arr = [[] for _ in range(N+1)]
#     for i in range(M):
#         x, y = map(int, input().split())
#         Arr[x].append(y)
#         Arr[y].append(x)
#
#     res = 0
#     visited = [False] * (N + 1)
#     for j in range(1,N+1):
#
#         dfs(j, 1)
#
#     print(f'#{tc} {res}')


def dfs(start, cnt):
    global max_cnt
    visited[start] = True
    if cnt > max_cnt:
        max_cnt = cnt

    for node in graph[start]:
        if not visited[node]:
            dfs(node, cnt + 1)

    visited[start] = False


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (N + 1)

    max_cnt = 0
    for i in range(1, N + 1):
        dfs(i, 1)

    print('#{} {}'.format(t, max_cnt))

# def dfs(x):
#     global res
#     cnt = 0
#     st = []
#     st.append(x)
#
#     while st:
#         v = st.pop()
#         if not visited[v]:
#             cnt += 1
#             visited[v] = True
#             if cnt > res:
#                 res = cnt
#             for w in Arr[v]:
#                 if not visited[w]:
#                     st.append(w)

