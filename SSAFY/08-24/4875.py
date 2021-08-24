import sys
sys.stdin = open('input.txt', 'r')



# visited 를 2차원 배열로 만듬
# def dfs(curi, curj):
#     st = []
#     visited = [[0] * N]
#     st.append(curi, curj)  # v대신에 curi, curj
#     visited[v] = True      # 방문 첫번째 : 2차원 배열로 방문 여부를 만든다. 두번째 방법은 길을 벽으로 바꾼다.
#
#     while st:
#         v = st.pop()
#         print(v)
#         for w in 인접한 벽이면 못감 미로 밖으로 못나감감
#             if not visited[w]:
#                 st.append(w)
#                 visited[w] = True
#             # else:    필요 없는거 같다
#             #     v = st.pop()

#visited를 벽으로 만듬
def dfs(curi, curj):
    di = [0, 0, 1, -1]    # 우좌하상
    dj = [1, -1, 0, 0]
    st = []

    st.append((curi, curj))
    Arr[curi][curj] = 1

    while st:
        (curi, curj) = st.pop()
        for d in range(4):
            newi = curi + di[d]
            newj = curj + dj[d]
            if 0 <= newi < N and 0 <= newj < N and Arr[newi][newj] == 3:  #3도 따로 처리해주자
                return 1
            if 0 <= newi < N and 0 <= newj < N and Arr[newi][newj] == 0:
                st.append((newi, newj))
                Arr[newi][newj] = 1

    return 0

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    Arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Arr[i][j] == 2:
                curi, curj = i, j
    print('#{} {}'.format(tc,dfs(curi, curj)))


    # 원래 Arr 입력받은 방법인데 아래 방법이 더 깔끔하고 편한거 같다.
    # Arr = [[0] * N for _ in range(N)]
    # for n in range(N):
    #     text = input()
    #     for k in range(N):
    #         Arr[n][k] = int(text[k])