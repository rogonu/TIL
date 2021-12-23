import sys
sys.stdin = open('in1.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    # ARR = [[0]*N for _ in range(N)]
    ARR = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(len(ARR)):
    #     for j in range(len(ARR[i])):
    #         ARR[i,j] =
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    print(ARR)
    sum_v = 0
    for x in range(len(ARR)):

        for y in range(len(ARR[x])):

            for i in range(4):

                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N :
                    continue
                else:
                    sum_v += abs(ARR[x][y] - ARR[new_x][new_y])

    print(sum_v)