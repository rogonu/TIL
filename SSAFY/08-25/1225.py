import sys

sys.stdin = open('input.txt', 'r')


def cycle():
    while que[-1] > 0:
        for i in range(1, 6):
            if que[0] - i > 0:
                que.append(que.pop(0) - i)
            else:
                que.pop(0)
                que.append(0)
                return que


for _ in range(10):
    tc = int(input())
    que = list(map(int, input().split()))
    print('#{} {}'.format(tc, ' '.join(map(str, cycle()))))
