def chk(lst, key):
    l = 0
    r = len(lst) - 1
    di = 0
    while l <= r:
        m = (l + r) // 2
        if key == lst[m]:
            return 1
        if key < lst[m]:
            if di == 'L':
                return 0
            r = m - 1
            di = 'L'
        else:
            if di == 'R':
                return 0
            l = m + 1
            di = 'R'
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for key in B:
        cnt += chk(A, key)
    print(f'#{tc} {cnt}')