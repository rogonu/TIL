import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1,TC+1):
    K, N, M = map(int, input().split())
    battery = list(map(int,input().split()))
    curp = 0
    cnt = 0
    while curp < N:
        nextp = curp +K
        if nextp >= N:
            break
        if nextp not in battery:
            while curp < nextp and nextp not in battery:
                nextp -= 1
            if curp == nextp:
                cnt = 0
                break
        cnt += 1
        curp = nextp
    print(cnt)
        # if nextp in battery:
        #     cnt += 1
        #     curp = nextp
        # else:
        #     while curp < nextp and nextp not in battery:
        #         nextp = -1
        #     if curp == nextp:
        #         cnt = 0
        #         break
        #     else:
        #         cnt += 1
        #         curp = nextp
    # print(f'#{tc} {cnt}')
    #방법 2
    # curp = 0
    # while curp < N:
    #     nexp = curp +K
    #     if 충전기가 있나?:
    #         cnt += 1
    #         curp =nextp
    #     else:
    #         nexp 의 값을 하나씩 빼면서 충전기가 있는지 확인
    # 방법2
    # battery.insert(0,0)
    # battery.append(N)
    # lastp = 0
    # cnt = 0
    # for i in range(1, len(battery)):
    #     # 충전기 사이의 거리를 확인한다. 못가면 return 0
    #     if battery[i] - battery[i-1] > K:
    #         cnt = 0
    #         break
    #     # i번째에 있는 충전기에서 충전 여부 결정한다.
    #     if battery[i] > lastp + K:
    #         lastp = battery[i-1]
    #         cnt += 1
    #
    # print(cnt)