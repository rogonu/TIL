TC = int(input())
for tc in range(1, TC+1):
    T, P = input().split()
    N = len(T)
    M = len(P)
    cnt = 0
    idxT = 0
    while idxT < N-M+1:
        idxP=0
        while idxP < M and T[idxT+idxP] == P[idxP]:
            idxP += 1
        if idxP == M:
            cnt += 1
            idxT += M
        else:
            idxT += 1

    cnt = cnt + N - cnt * M
    print(f'#{tc} {cnt}')