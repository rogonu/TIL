import sys
sys.stdin = open('input.txt', 'r')

# 중복된 순열 까지 모두 구한거
# def soon(k):
#     if k == N:
#         print(t)
#     else:
#         for i in range(N):
#             t[k] = i
#             soon(k+1)

# 중복된 순열은 빼고
def soon(k, sum_v):
    global  min_V
    if sum_v > min_V:
        return
    if k == N:
        # for j in range(N):
        #     sum_v += Arr[j][t[j]]
        if min_V > sum_v:
            min_V = sum_v
    else:
        for i in range(N):
            if not visit[i]:
                visit[i] = True
                t[k] = i
                soon(k+1, sum_v + Arr[k][t[k]])
                visit[i] = False

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    t = [-1] * N
    visit = [False] * N
    sum_v = 0
    min_V = 10*N

    soon(0, sum_v)
    print(f'#{tc} {min_V}')