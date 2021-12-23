import sys
sys.stdin = open('input.txt', 'r')

def Check(text):
    s = []
    for i in text:
        if i == '(' or i == '{':
            s.append(i)
        elif i == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                return 0
        elif i == '}':
            if s and s[-1] == '{':
                s.pop()
            else:
                return 0
    if len(s) < 1:
        return 1
    else :
        return 0
TC = int(input())
for tc in range(1, TC + 1):
    text = input()
    print('#{} {}'.format(tc, Check(text)))