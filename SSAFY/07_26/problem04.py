# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = []
    for i in word:                                  # word 의 값을 각가 10진수의 값으로 바꾼후 a에 저장한다.
        a.append(ord(i))
    
    b = []                                   # 소문자는 소문자끼리 대문자는 대문자끼리 바뀌어야 하므로 소문자와 대문자로 나누어 조건을 걸어준다.
    for j in a:                              # 대문자의 경우 j + n 이 90을 넘으면 대문자가 안나오므로 90을 넘었을시 65로 돌아가게 해준다
        if 65<=j<=90:                        # 소문자의 경우 j + n 이 122를 넘으면 소문자가 안나오므로 122를 넘었을시 97로 돌아가게해준다.
            if j+n > 90:                     # n만큼 바뀐 숫자를 b에 저장해준다
                b.append(j+n-26)
            else:
                b.append(j+n)
        elif 97<= j <=122:
            if  j+n >122:
                b.append(j+n-26)
            else:
                b.append(j+n)
    res = ''                                # b에 저장된 값을  chr()을 이용하여 다시 알파벳으로 바꾸어준다.
    for k in b:
        res += chr(k)
    return res
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx