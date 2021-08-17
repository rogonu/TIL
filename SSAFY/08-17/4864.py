import sys
sys.stdin = open('input4684.txt', 'r')
def bm(P, T):
    M = len(P)
    N = len(T)
    skip =  [M] * 128
    for i in range(M-1):
        skip[ord(P[i])] = M - i -1

    idxT = 0
    while idxT <= N - M:
        idxP = M - 1
        while idxP >= 0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return idxT
        idxT = idxT + skip[ord(T[idxT+ M - 1])]
    return -1
TC = int(input())
for tc in range(1, TC +1):
    A = input()
    B = input()
    # if bm(A, B) == -1:
    #     res = 0
    # else:
    #     res = 1
    # print(f'#{tc} {res}')
    if A in B:
        print(1)
    else: print(0)