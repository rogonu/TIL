import sys
sys.stdin = open('input.txt','r')


TC = int(input())
def my_max(x):
    max_v = x[0]
    for i in range(len(x)):
        if x[i] > max_v:
            max_v = x[i]
    return max_v
def my_min(x):
    min_v = x[0]
    for i in range(len(x)):
        if x[i] < min_v:
            min_v = x[i]
    return min_v
for tc in range(1, TC+1):
    N = int(input())
    num = list(map(int, input().split()))
    # max_v = 0
    # for i in range(len(num)):
    #     for j in range(i+1,len(num)):
    #         if abs(num[i] - num[j]) > max_v:
    #             max_v = abs(num[i] - num[j])
    # print(f'#{tc} {max_v}')
    max_v = my_max(num)
    min_v = my_min(num)
    result = max_v - min_v
    print(f'#{tc} {result}')