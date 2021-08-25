import sys

sys.stdin = open('input.txt', 'r')
def cal():
    st = []
    for i in num:
        if i == '+':
            if len(st) < 2:
                return 'error'
            st.append(st.pop() + st.pop())
        elif i == '-':
            if len(st) < 2:
                return 'error'
            st.append(st.pop(-2) - st.pop())
        elif i == '*':
            if len(st) < 2:
                return 'error'
            st.append(st.pop() * st.pop())
        elif i == '/':
            if len(st) < 2:
                return 'error'
            st.append(st.pop(-2) / st.pop())
        elif i == '.':
            if len(st) != 1:
                return 'error'
            return int(st.pop())
        else:
            st.append(int(i))
TC = int(input())
for tc in range(1, TC + 1):
    num = list(input().split())
    print('#{} {}'.format(tc, cal()))
    # for i in num:
    #     if i == '+':
    #         st.append(st.pop() + st.pop())
    #     elif i == '-':
    #         st.append(st.pop(-2) - st.pop())
    #     elif i == '*':
    #         st.append(st.pop() * st.pop())
    #     elif i == '/':
    #         st.append(st.pop(-2) / st.pop())
    #     elif i == '.':
    #         print(st.pop())
    #     else:
    #         st.append(int(i))
