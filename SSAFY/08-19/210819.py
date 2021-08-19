import sys
sys.stdin = open('input.txt', 'r')

TC = 10
for tc in range(TC) :
    T , N = map(int, input().split())
    G = [[] for _ in range(100)]
    path = list(map(int, input().split()))
    for i in range(0, N, 2):
        G[path[i]].append(path[i+1])
    print(G)


