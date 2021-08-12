def isFind(col):
    curR = 0
    curC = col
    while :
        if 왼쪽에 길이 있으면 영역을 벗어 나도 안됨:
            d = -1
            curC -= 1
        elif 오른쪽에 길이 있으면 :
            d = 1
            curC += 1
        else:
            curR += 1




    if ARR[curR][curC] == 2:
        return True
    else:
        return False
for i in range(100):
    if ARR[0][i] == 1:
        if isFind(i):
            result = i
            break
print(f'#{tc} {result}')