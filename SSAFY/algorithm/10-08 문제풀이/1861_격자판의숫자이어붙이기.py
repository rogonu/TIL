di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
def find(x, y, res):
    global  result
    if len(res) == 7:
        result.add(res)
        return
    res = res + lst[x][y]
    for k in range(4):
        new_i = x + di[k]
        new_j = y + dj[k]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            find(new_i, new_j, res)

TC = int(input())
for tc in range(1, TC + 1):
    lst = [list(input().split()) for _ in range(4)]
    result = set()
    res = ''
    for i in range(4):
        for j in range(4):
            find(i, j, res)
    print(f'#{tc} {len(result)}')
