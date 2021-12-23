import sys
sys.stdin = open('input.txt', 'r')

# def rem(t):
#     s = [t[0]]
#     for i in t:
#         if s[-1] != i:
#             s.append(i)
#         else:
#             s.pop()
#     return s



TC = 10
for tc in range(1, TC+1):
    N, text = input().split()
    lst = list(map(int, text))
    s = [lst[0]]
    for i in range(1,len(lst)):
        if not s:
            s.append(lst[i])

        elif s[-1] != lst[i]:
            s.append(lst[i])
        else:
            s.pop()
    res = ''.join(map(str, s))
    print(f'#{tc} {res}')
