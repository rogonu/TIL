import sys


TC = 10
for tc in range(1, TC+1):
    NO = int(input())
    # BRD = [[0] * 100 for _ in range(100)]
    # for i in range(100):
    #     BRD[i] = list(map(int, input().split()))
    BRD = [list(map(int, input().split())) for _ in range(100)]

    # 행 우선 가로축 으로 보면서 각 해으이 합을 구해 maxv 구하기
    # 열 우선 으로 보면서 각 열의 합을 구해 maxv 구하기

    # 왼쪽으로 대각 (0,0) (1,1)(2,2)  ..... (99,99)
    for i in range(100:
        BRD[i][i]
    # 오른쪽 대각
    for i in range(100):
        BRD[i][N-1-i]