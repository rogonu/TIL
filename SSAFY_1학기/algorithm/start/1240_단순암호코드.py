patt = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(input())

    for row in range(N):
        if '1' in arr[row]:
            col = arr[row][::-1].index('1')
            break
    col = M - col - 56

    res = []
    for i in range(8):
        arr[row][col:col + 7]
        res.append(patt.index(arr[row][col:col+7]))
        col += 7
    sum_odd = res[0]+ res[2] + res[4] + res[6]
    sum_even = res[1] + res[3] + res[5] +res[7]
    if (sum_odd*3 + sum_even) % 10 == 0:
        print(f'#{tc} {sum_odd+sum_even}')
    else:
        print(f'#{tc} 0')    