import sys
sys.stdin = open('input4836.txt', 'r')

TC = int(input())
for tc in range (1, TC + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(10):
            for j in range(10):
                if r1<= i <= r2 and c1 <= j <= c2:
                    arr[i][j] += color

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                result += 1

    print(f'#{tc} {result}')

