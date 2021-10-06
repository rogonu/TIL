TC = int(input())
def solve(k):
    global maxv
    intv = int(''.join(pan))
    if k == N:
        if maxv < intv:
            maxv = intv
        return

    for i in range(720):
        if state[k][i] == 0:
            state[k][i] = intv
            break
        if state[k][i] == intv:
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
    state = [[0] * 720 for _ in range(N)]

    maxv = 0
    solve(0)
    print(maxv)
