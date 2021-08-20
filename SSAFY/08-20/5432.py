import sys
sys.stdin = open('input.txt', 'r')

def check():
    st = []
    result = 0
    cnt = 0
    for i in bar:
        if i == '(':
            st.append(i)
            result += 1
            cnt += 1
        elif st and i == ')':
            cnt -= 1
            result -= 1
            if st[-1] == '(':
                result += cnt
            st.pop()

    return result

TC = int(input())
for tc in range(1, TC +1):
    bar = input()
    print(f'#{tc} {check()}')
