import sys
sys.stdin = open('input4837.txt', 'r')

TC = int(input())
for tc in range (1, TC + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Bits = N
    result = 0
    for i in range(1<<Bits):
        sum_v = 0
        cnt = 0
        # print(i)
        for j in range(Bits):
            if i & (1<<j):
                # print(lst[j], end = ' ')
        # print()
                sum_v += A[j]
                cnt += 1
    # if sum_v == K:
    #     result += 1
        print(i, cnt, sum_v)
    # print(result)