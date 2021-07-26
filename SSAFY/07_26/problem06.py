# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def rock_paper_scissors(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    res = []
    for i in range(len(data)):            # 반복문을 이용하여 data[i][0]의 값은 A가 낸것 data[i][1]의 값은 B가 낸것이므로
        if data[i][0] == 0:               # data[i][0]가 가위 일때 바위일때 보일 때 값에 따라서 draw냐 A가 이기냐 B가 이기냐를 구하고
            if data[i][1] == 0:           # 결과를 res 에 더해준다.
                res.append('draw')       
            elif data[i][1] == 1:
                res.append('B')
            elif data[i][1] == 2:
                res.append('A')
        if data[i][0] == 1:
            if data[i][1] == 0:
                res.append('A')
            elif data[i][1] == 1:
                res.append('draw')
            elif data[i][1] == 2:
                res.append('B')
        if data[i][0] == 2:
            if data[i][1] == 0:
                res.append('B')
            elif data[i][1] == 1:
                res.append('A')
            elif data[i][1] == 2:
                res.append('draw')
   
    res_2 = 0                     # 가위바위보의 결과를 A가 이겼으면 +1 B가 이겼으면 -1 draw 일 경우에는 그대로 를 이용하여
    for i in res:                 # 가위바위보의 결과를 점수로 표현한다. 점수가 >+ 1 이면 A가 더 많이 이겼고 0 이면 무승부 >=1이면 B가 더 많이 이건것이므로
        if i == 'A':              # 그 결과를 반환한다.
            res_2 += 1
        elif i == 'B':
            res_2 -= 1
        elif i == 'draw':
            res_2 = res_2
    if res_2 >= 1:
        return 'A'
    elif res_2 == 0:
        return 'draw'
    elif res_2 <= -1:
        return 'B'    
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(rock_paper_scissors([[0, 1], [1, 2], [2, 2]]))
    # B
    print(rock_paper_scissors([[0, 1], [1, 0]]))
    # draw