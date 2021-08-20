import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    s = []
    visited = [False] * (100)

    visited[v] = True
    s.append(v)
    while s:
        v = s.pop()
        if v== 99:
            return 1
        for w in G[v] :
            if visited[w] == False:
                s.append(w)
                visited[w] = True
    return 0
TC = 10
for tc in range(TC) :
    T , N = map(int, input().split())
    G = [[] for _ in range(100)]
    path = list(map(int, input().split()))
    for i in range(0, 2 * N, 2):
        G[path[i]].append(path[i+1])
    print('#{} {}'.format(T, dfs(0)))


