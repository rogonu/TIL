def combi(N, M, k, s):
    if k == M:
        B=

        for i in range(s, N-M+k+1):
            res[k] = i
            combi(N, M, k+1, i+1)

res = [-1] * M
T = [0,1,2,3]
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]