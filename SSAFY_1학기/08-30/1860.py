import sys

sys.stdin = open('input.txt', 'r')

def check():
    for i in range(len(arrive)):
        t = i // K + 1
        if arrive[i]//M < t:
            return 'Impossible'
    else:
        return 'Possible'
TC = int(input())
for tc in range(1, TC + 1):
    N, M , K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()

    print('#{} {}'.format(tc,check()))