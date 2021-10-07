def solve(k, remain, s):
    global cnt
    if s >= cnt:
        return
    if remain == 0:
        return
    if k == busstop[0]:
        if s < cnt:
            cnt = s
        return


    solve(k+1, busstop[k+1], s + 1)
    solve(k+1, remain -1, s)

TC = int(input())
for tc in range(1, TC + 1):
    busstop = list(map(int, input().split())) + [0]
    cnt = 100
    solve(1, busstop[1], 0)

    print(f'#{tc} {cnt}')