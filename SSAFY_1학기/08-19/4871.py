import sys
sys.stdin = open('input.txt', 'r')


def dfs(v):
    s = []
    visited = [False] * (V+1)

    visited[v] = True
    s.append(v)
    while s:
        v = s.pop()
        if v==G:
            return 1
        for w in Arr[v] :
            if visited[w] == False:
                s.append(w)
                visited[w] = True
    return 0

TC = int(input())
for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    Arr = [[] for _ in range(V + 1)]
    for e in range(E):
        i, j = map(int, input().split())
        Arr[i].append(j)
    S, G = map(int, input().split())

    print(f'#{tc} {dfs(S)}')
    # print(dfs(S))