import sys
sys.stdin = open('input.txt')

TC = 10
for tc in range(1,TC+1):
    N = input()
    lst = list(map(int,input().split()))
    cnt = 0
    for i in range(2,len(lst)-2):
        # if lst[i] >= lst[i-2] and lst[i] >= lst[i - 1] and\
        #     lst[i] >= lst[i + 1] and lst[i] >= lst[i + 2] :
        #     cnt += lst[i]-max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
        highest = 0
        for j in (lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            if j >= highest:
                highest = j
        if lst[i] > highest:
            cnt += lst[i] - highest
    print(f'#{tc} {cnt}')
