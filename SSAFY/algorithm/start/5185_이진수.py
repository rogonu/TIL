TC = int(input())
for tc in range(1, TC + 1):
    N , Hexa = input().split()
    res = ''
    for i in Hexa:
        if i.isdigit():
            num_v = int(i)
        else:
            num_v = ord(i) - ord('A') + 10
                
        for j in range(3,-1,-1):
            if num_v & (1 << j):
                res += '1'
            else:
                res += '0'

    print(f'#{tc} {res}')
