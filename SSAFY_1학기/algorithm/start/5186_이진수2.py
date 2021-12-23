TC = int(input())
for tc in range(1, TC + 1):
    N = float(input())
    num = 1
    cnt = 0
    res = ''
    while cnt < 14:
        if N >= 2 ** (-1 * num):
            N -= 2 ** (-1 * num)
            res += '1'
        else:
            res += '0'
        if N == 0:
            break
        num += 1
        cnt += 1
    if len(res) < 13:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} overflow')
