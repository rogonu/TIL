import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = list(k for k in range(M))
    que = []
    for i in range(N):
        que.append(pizza.pop(0))
    while que:
        for j in range(len(que)):
            cheese[que[j]] = cheese[que[j]] // 2
        for l in range(len(que)):
            if cheese[que[l]] == 0:
                que.pop(l)
                if pizza:
                    que.append(pizza.pop(0))


    print(cheese)

