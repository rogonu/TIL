def makeT(idx):
    if idx == 1:
        return
    if tree[idx] < tree[idx//2]:
        tree[idx], tree[idx //2] = tree[idx // 2] , tree[idx]
        makeT(idx//2)
#반복문으로
def getSum():
    sumV = 0
    idx = N // 2
    while idx >= 1:
        sumV += tree[idx]
        idx //= 2
    return sumV

# 재귀로
# def getSum2(idx):
#     global sumV2
#     if idx:
#         sumV2 += tree[idx]
#         getSum2(idx//2)

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    tree = [0] * (N+1)
    for i in range(1, N+1):
        tree[i] = lst[i]
        makeT(i)
    sumV2 = 0    
    print(f'#{tc} {getSum()}')