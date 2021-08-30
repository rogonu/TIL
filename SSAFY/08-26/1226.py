import sys

sys.stdin = open('input.txt', 'r')


def bfs(curi, curj):
    st = []
    st.append((curi, curj))
    while st:
        curi, curj = st.pop(0)
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            newi = curi + di
            newj = curj + dj
            if Arr[newi][newj] == 0:
                st.append((newi, newj))
                Arr[newi][newj] = 1
            elif Arr[newi][newj] == 3:
                return 1
    return 0


for _ in range(10):
    tc = int(input())
    Arr = [list(map(int, input())) for _ in range(16)]
    print('#{} {}'.format(tc, bfs(1, 1)))
