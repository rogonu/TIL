import sys

sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    Arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if Arr[i][j] == 'A':
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    newi = i + x
                    newj = j + y
                    if 0 <= newi < n and 0 <= newj < n and Arr[newi][newj] == 'H':
                        Arr[newi][newj] = 'O'
    cnt = 0
    for s in range(n):
        for d in range(n):
            if Arr[s][d] == 'H':
                cnt += 1
    print(cnt)
