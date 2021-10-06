def prt():
    for i in range(N):
        if res[i] ==1:
            print(lst[i], end = ' ')
    print()

#부분집합 구하기
def powerset(k, sumv):

    if sumv > 15:
        return

    if k == N:
        sumv = 0
        for i in range(N):
            if res[i] == 1:
                sumv += lst[i]
        if sumv == 15:
            prt()
        return
    res[k] = 0
    powerset(k+1,sumv)

    res[k] = 1
    powerset(k + 1, sumv + lst[k])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
N = len(lst)
res = [-1] * N

powerset(0, 0)