TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = []
    for i in range(len(won)):
        cnt = 0
        while N >= won[i]:
            N = N - won[i]
            cnt += 1
        res.append(cnt)
    print(f'#{tc}')
    print(*res)