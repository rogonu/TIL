isp = {'+' : 1, '*' : 2}
icp = {'+' : 1, '*' : 2}

def step1(s):
    temp = []
    st = []
    for c in s:
        if c in ['+', '*',]:
            if not st or icp[c] > isp[st[-1]]:
                st.append(c)

            else:
                while st and isp[st[-1]] >= isp[c]:
                    temp.append(st.pop())
                st.append(c)
        else:
            temp.append(c)
    while st:
        temp.append(st.pop())
    if not st:
        return temp

    # for i in range(len(st)):
    #     print(st.pop(), end=' ')
    #     temp.append(st.pop())
    #
    # return temp

def step2(temp):
    st = []
    for i in temp:
        if i =='+':
            st.append(int(st.pop())+int(st.pop()))
        elif i == '*':
            st.append(int(st.pop())*int(st.pop()))
        else:
            st.append(i)
    return st.pop()
TC = 10
for tc in range(1, TC+1):
    N = int(input())
    s = input()
    print('#{} {}'.format(tc, step2(step1(s))))
