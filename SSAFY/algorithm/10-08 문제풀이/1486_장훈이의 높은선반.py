def solve(x,  sum):
    global min_v
    if x == N :
        if B <= sum < min_v:
            min_v = sum
        return

    solve(x + 1,  sum)
    solve(x + 1, sum+H[x])



TC = int(input())
for tc in range(1, TC + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_v = 9999999999999999999
    solve(0,0)
    res = min_v - B
    print(f'#{tc} {res}')