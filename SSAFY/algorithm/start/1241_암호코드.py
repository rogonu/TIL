import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
Patt = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]
# def hexToBinStr(x):
#     dict = {'0': '0000', '1' : '0001', '2': '0010',
#             '3' : '0011', '4' : '0100', '5' : '0101',
#             '6' : '0110', '7' : '0111', '8': '1000',
#             '9' : '1001', 'A' : '1010', 'B' : '1011',
#             'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111' }

#     return dict[x]
def hexToBinStr(arr):
    #arr = '0269FAC9A0'
 
    arr = arr.replace('0', '0000')
    arr = arr.replace('1', '0001')
    arr = arr.replace('2', '0010')
    arr = arr.replace('3', '0011')
    arr = arr.replace('4', '0100')
    arr = arr.replace('5', '0101')
    arr = arr.replace('6', '0110')
    arr = arr.replace('7', '0111')
    arr = arr.replace('8', '1000')
    arr = arr.replace('9', '1001')
    arr = arr.replace('A', '1010')
    arr = arr.replace('B', '1011')
    arr = arr.replace('C', '1100')
    arr = arr.replace('D', '1101')
    arr = arr.replace('E', '1110')
    arr = arr.replace('F', '1111')
 
    return arr
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Arr = [input() for _ in range(N)]
    for i in range(N):
        Arr[i] = hexToBinStr(Arr[i][0:M])
    
    sum_v = 0
    for row in range(1, N):
        if Arr[row].find('1') < 0:
            continue
        col = M * 4 - 1
        while col > 56:
            if Arr[row][col] == '1' and Arr[row-1][col] == '0':
                res = []
                for i in range(8):
                    cnt1 = cnt2 = cnt3= 0
                    while Arr[row][col] == '1':
                        cnt1 += 1
                        col -= 1
                    while Arr[row][col] == '0':
                        cnt2 += 1
                        col -= 1
                    while Arr[row][col] == '1':
                        cnt3 += 1
                        col -= 1
                    while col >= 0 and Arr[row][col] == '0':
                        col -= 1

                    r = min(cnt1, cnt2, cnt3)
                    res.insert(0,Patt.index(cnt3 //r * 100 + cnt2//r *10 + cnt1//r))
                
                odd_v = res[0] + res[2] + res[4] + res[6]
                even_v = res[1] + res[3] + res[5]+ res[7]

                if (odd_v * 3 + even_v) % 10 == 0:
                    sum_v += sum(res)
            else:
                col -= 1        
    print(f'#{tc} {sum_v}')