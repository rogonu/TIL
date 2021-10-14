def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])
def union(x,y):

    p[find_set(y)] = find_set(x)

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    p = [i for i in range(N + 1)]

    for i in range(M):
        s1 = lst[i*2]
        s2 = lst[i*2+1]
        union(s1,s2)
    cnt = [0] * (N+1)
    for i in range(1, N + 1):
        cnt[find_set(i)] = 1
    print(f'{tc} {sum(cnt)}')


# dfs 이용한방법

def dfs(curv):
    visited[curv] = True

    for newv in G[curv]:
        if not visited[newv]:
            dfs(newv)

TC = int(input())
for tc in range(1, TC + 1):
    N, M =int(input())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(M):
        s1= lst[i*2]
        s2 = lst[i*2 +1]
        G[s1].append(s2)
        G[s2].append(s1)

    cnt = 0
    visited = [False] * (N+1)
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)