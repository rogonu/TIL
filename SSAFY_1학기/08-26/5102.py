import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())


def bfs(v):
    que = []
    visited = [0] * (V + 1)
    que.append(v)
    visited[v] = 1
    while que:
        v = que.pop(0)

        for w in L[v]:
            if not visited[w]:
                que.append(w)
                visited[w] = visited[v] + 1
    if visited[G]:
        return visited[G] - 1
    return visited[G]


for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    L = [[] for _ in range(V + 1)]
    for e in range(E):
        v1, v2 = map(int, input().split())
        L[v1].append(v2)
        L[v2].append(v1)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, bfs(S)))
