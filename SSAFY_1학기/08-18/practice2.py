def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return -1
    else:
        return s.pop(-1)

s1 = '()()((()))'
s2 = '(()'
s3 = '())'
st = []
result ='OK'
for c in s3:
    if c == '(':
        st.append(c)
    else:
        if len(st) == 0:
            result = 'ERR'
        else:
            st.pop(-1)
if len(st) != 0:
    result = 'ERR'
print(result)
