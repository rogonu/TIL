import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    text = input()
    st= [0]
    for i in text:
        if i != st[-1]:
            st.append(i)
        else:
            st.pop()
    print(f'#{tc} {len(st)-1}')