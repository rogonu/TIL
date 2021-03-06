lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = {0:[], 1:[2, 3], 2:[1, 4, 5], 3:[1, 7], 4:[2, 6], 5:[2, 6], 6:[4, 5, 7], 7:[3, 6]}
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   #1
    [0, 1, 0, 0, 1, 1, 0, 0],   #2
    [0, 1, 0, 0, 0, 0, 0, 1],   #3
    [0, 0, 1, 0, 0, 0, 1, 0],   #4
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0]
]

#v의 방문하지 않은 정점을 하나 찾아서 return한다.

#방문하지 않은 정점이 없으면 -1 을 retrun
def findW1(v):
    for i in range(0, len(lst), 2):
        v1 = lst[i]
        v2 = lst[i+1]
    # if v == lst[i] and visited[lst[i+1]]==False:
    #     return lst[i+1]
    if v == v1 and visited[v2]==False:
         return v2

    if v == lst[i+1] and visited[lst[i]]==False:
        return lst[i]
    return -1

def findW2(v):

    #print(G[v])
    for w in G[v]:
        if visited[w]==False:
            return w

    return -1

def findW(v):

    # for i in range(len(adj[v])):
    #     if adj[v][i]==1 and visited[i]==False:
    #         return i
    #
    # return -1

    lst = adj[v]
    for i in range(len(lst)):
        if lst[i]==1 and visited[i]==False:
            return i

    return -1
n = 7
visited = [False] * (n+1)   #0번 비워놓는다
ST = []
# def dfs(v):
#     visited[v] = True
#     print(v)
#     ST.append(v)
#     while len(ST) > 0:
#         w = findW(v)
#         if w != -1:
#             ST.append(v)
#             visited[w] = True
#             print(w)
#             v = w
#         else:
#             v = ST.pop(-1)
# def dfs(v):
#     s = []
#     s.append(v)
#     while s:
#         v = s.pop(-1)
#         if not visited[v]:
#             print(v, end=' ')
#             visited[v] = True
#             for w in G[v]:
#                 if not visited[w]:
#                     s.append(w)
# 뒤에 순서가 꼬임
def dfs(v):
    s = []
    s.append(v)
    visited[v] = True
    while s:
        v = s.pop(-1)
        print(v, end=' ')
        for w in G[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = True
#재귀함수
# def dfs(v):
#     visited[v] = True
#     print(v, end =' ')
#     for w in G[v]:
#         if not visited[w]:
#             dfs(w)
dfs(1)

