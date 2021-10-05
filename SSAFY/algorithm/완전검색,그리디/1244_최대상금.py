TC = int(input())
def solve(k):
    global maxv
    if k == N:
        intv = int(''.join(pan))
        if maxv < intv:
            maxv = intv
        return

    L = len(pan)
    for i in range(0, L - 1):
        for j in range(i + 1, L):
            pan[i], pan[j] = pan[j], pan[i]
            solve(k+1)
            pan[i], pan[j] = pan[j], pan[i]
for tc in range(1, TC + 1):
    pan, N = input().split()
    pan = list(pan)
    N = int(N)
    maxv = 0
    solve(0)
    print(maxv)
