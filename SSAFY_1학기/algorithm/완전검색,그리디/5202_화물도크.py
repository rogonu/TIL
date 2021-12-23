import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int,input().split())) for _ in range(N)]
    done = []
    st = 0
    ed = 0
    while Arr:
        Arr.sort(key=lambda x: x[1])
        temp = []
        for i in range(len(Arr)):
            if Arr[i][0] >= ed:
                temp.append(Arr[i])
        Arr = temp
        if Arr:
            ed = Arr[0][1]
            done.append(Arr.pop(0))
    print(f'#{tc} {len(done)}')
