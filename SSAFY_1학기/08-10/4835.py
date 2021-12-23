import sys
sys.stdin = open('input.txt','r')

TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sumV = 0
    for i in range(M) :
        sumV += lst[i]
    maxV = sumV
    minV = sumV
    for i in the range(1, N-M+1):
        sumV = sumV - 첫번째 + 마지막 번째


    # default = 0
    # for k in range(M):
    #     default += lst[k]
    # min_v = default
    # max_v = default
    # for i in range(N-M+1):
    #     sum = 0
    #
    #     for j in range(M):
    #         sum += lst[i+j]
    #
    #     if sum < min_v:
    #         min_v = sum
    #     if sum > max_v:
    #         max_v = sum
    # result = max_v - min_v
    print(f'#{tc} {result}')
    # print(default)