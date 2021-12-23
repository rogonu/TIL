
import sys
sys.stdin = open('input.txt', 'r')

# 1 = 가위 2 = 바위 3 = 보


def game(i, j):
    if i == j:
        return i

    n = game(i, (i + j) // 2)
    m = game((i + j) // 2 + 1, j)
    if player[n] == player[m]:
           return n
    elif player[n] == 1:
        if player[m] == 2:
            return m
        elif player[m] == 3:
            return n
    elif player[n] == 2:
        if player[m] == 1:
            return n
        elif player[m] == 3:
            return m
    elif player[n] == 3:
        if player[m] == 1:
            return m
        elif player[m] == 2:
            return n


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    player = [0] + lst
    print(f'#{tc} {game(1, N)}')


# 뭐가 틀렸을까 생각해보았는데 변수명을 잘못 입력했음
# def game(i, j):
#     if i == j:
#         return i
#
#     game_1 = game(i, (i + j) // 2)
#     game_2 = game((i + j) // 2 + 1, j)
#     if player[i] == player[j]:
#            return i
#     elif player[i] == 1:
#         if player[j] == 2:
#             return j
#         elif player[j] == 3:
#             return i
#     elif player[i] == 2:
#         if player[j] == 1:
#             return i
#         elif player[j] == 3:
#             return j
#     elif player[i] == 3:
#         if player[j] == 1:
#             return j
#         elif player[j] == 2:
#             return i