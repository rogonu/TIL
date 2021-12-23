import sys
sys.stdin = open('input4839.txt', 'r')

def binary(P, S):
    l = 1
    r = P
    cnt = 0
    while l <= r:
        c = int((l+r)/2)
        if c == S:
            return cnt
        elif c < S:
            l = c
        else:
            r = c
        cnt += 1
    return -1
TC = int(input())
result = 0
for tc in range (1, TC + 1):
    P, A, B = map(int, input().split())
    cnt_A = binary(P, A)
    cnt_B = binary(P, B)
    if cnt_A == cnt_B:
        result = 0
    elif cnt_A < cnt_B:
        result = 'A'
    else:
        result = 'B'

    print(f'#{tc} {result}')