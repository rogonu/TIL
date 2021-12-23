import sys
sys.stdin = open('input4865.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    dict = {}
    for i in str1:
        dict[i] = 0
    for k, v in dict.items():
            for j in str2:
                if k == j:
                    v += 1
            dict[k] = v
    res = 0
    for value in dict.values():
        if value > res:
            res = value
    print(f'#{tc} {res}')