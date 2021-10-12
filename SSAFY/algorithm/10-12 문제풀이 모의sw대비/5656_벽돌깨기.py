import copy

def drop(pos):
    st =[]
    #세로 위치를 찾는다
    row = 0
    while row <H and blocks[row][pos] == 0:
        row += 1
    if row == H:
        return
    #블록 제거
    st.append((pos, row))
    while st:
        cur_r, cur_c = st.pop()
        size = blocks[cur_r][cur_c]
        blocks[cur_r][cur_c] = 0
        for i in range(size):
            if cur_c i < H and blocks[cur_r][cur_c]:
            #상:
            st.append((cur_r,cur_c - i))
            #하:
            st.append((cur_r, cur_c + i))
            # 좌:
            st.append((cur_r - i, cur_c ))
            # 우:
            st.append((cur_r + i, cur_c))
def solve(k):
    if k == N:
        return
    for i in range(W):
        #blocks 백업
        tmpblocks = copy.deepcopy(blocks)
        res[k] = i
        drop(i)
        solve(k+1)
        blocks = copy.deepcopy(tmpblocks)


TC = int(input())
for tc in range(1, TC + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    res = [-1]* W
    solve(0)