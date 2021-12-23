import sys
sys.stdin = open('input.txt','r')

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    card = list(map(int, input()))
    cnt = [0] * 10
    for i in card:
        cnt[i] += 1
    result = cnt[0]
    pos = 0
    for j in range(len(cnt)):
        if result <= cnt[j]:
            result = cnt[j]
        if cnt[j] == result:
            pos = j
    print(f'#{tc} {pos} {result}')
