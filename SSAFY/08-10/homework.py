import sys
sys.stdin = open('input.txt', 'r')

def minvalue():
    minv = box[0]
    for i in range(1, len(box)):
        if minv > box[i]:
            minv = box[i]
    return minv
def maxvalue():
    maxv = box[0]
    for i in range(1, len(box)):
        if maxv < box[i]:
            maxv = box[i]
    return maxv
def dump():
    minv = minvalue()
    maxv = maxvalue()
    minv += 1
    minv -= 1

TC= 10
for tc in range(1, TC+1):
    dcnt = int(input())
    box = list(map(int, input().split()))

    for i in range(dcnt):
        dump()
    result = maxvalue() - minvalue()
    print(result)



# 함수로 구하면 반복적으로 max min 처리를 위하여 dump 횟수만큼 수행하는데 이를 해결학 ㅣ위해 count 배열 활용해보자자