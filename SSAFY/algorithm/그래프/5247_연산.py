from collections import deque
def bfs():
    Q = deque()
    Q.append((N,0))
    while Q:
        curv,cnt = Q.popleft()
        if curv == M:
            return cnt
        t= [curv+1, curv-1, curv*2, curv-10]
        for newv in t:
            if 0 < newv <= 1000000 and not visited[newv]:
                visited[newv] =True
                Q.append((newv, cnt + 1))

TC = int(input())
for tc in range(1, TC + 1):
    N, M =map(int, input().split())
    visited = [False] * 1000001
    print(f'#{tc} {bfs()}')