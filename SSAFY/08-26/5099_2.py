import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    ci = [0] + list(map(int, input().split()))

    q = [0] * N
    newpizza = 1
    while q:
        pizza = q.pop(0)
        ci[pizza]= ci[pizza] // 2

        if ci[pizza] == 0:
            if newpizza <= M:
                q.append(newpizza)
                newpizza += 1
        else:
            q.append(pizza)
    print('#{} {}'.format(tc, pizza))
