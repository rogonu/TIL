import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int,input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    moved=[]
    container.sort(reverse=True)
    truck.sort(reverse=True)
    for i in range(len(container)):
        # if container[i] != 101:
        for j in range(len(truck)):
            if container[i] <= truck[j]:
                moved.append(container[i])
                container[i] = 101
                truck[j] = 0
                break
    print(f'#{tc} {sum(moved)}')