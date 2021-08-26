import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    que = list(map(int, input().split()))

    # for _ in range(M):
    #     que.append(que.pop(0))


    # counting 해서 구하기
    cnt = 0
    for _ in range(M):
        cnt = (cnt + 1) % N

    print('#{} {}'.format(tc, que[cnt]))
