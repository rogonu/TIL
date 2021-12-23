import sys

sys.stdin = open('input.txt', 'r')


def cnt(n):
    if n == 10:
        return 1
    if n == 20:
        return 3
    else:
        return cnt(n - 10) + 2 * cnt(n - 20)

Arr = [0] * 31
Arr[1] = 1
Arr[2] = 3
for i in range(3, 31):
    Arr[i] = Arr[i-1] + 2 * Arr[i-2]
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print(f'#{tc} {Arr[N//10]}')
