import sys
sys.stdin = open('input4861.txt', 'r')


def isCheck(str):
    # 슬라이싱 기법 사용
    # if str == str[::-1]:
    #     return True
    # else:
    #     return False
    # 반복문 사용
    for i in range(len(str) // 2):
        if str[i] != str[-1 -i]:
            return False
    return True
def checkRow():
    for row in range(N):
        for st in range(N-M+1):
            result = isCheck(Arr[row][st:st + M])
            if result:
                return Arr[row][st:st +M]
def checkColumn():
    for i in range(N):
        column = ''
        for j in range(N):
            column += Arr[j][i]
        for st in range(N-M+1):
            result = isCheck(column[st: st +M])
            if result:
                return column[st:st + M]
    # 교수님이 알려준 세로
    # for  col in range(N):
    #     for st in range(N-M+1):
    #         temp_str = ''
    #         for k in range(st, st+M):
    #             temp_str += Arr[k][col]
    #         result = isCheck(temp_str)
    #         if result:
    #             return temp_str

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Arr = [input() for _ in range(N)]
    if checkRow():
        res = checkRow()
    elif checkColumn():
        res = checkColumn()
    print(f'#{tc} {res}')