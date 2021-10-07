def quicksort(lst, l, r):
    if l >= r:
        return
    s = partition(lst, l, r)
    quicksort(lst, l, s -1)
    quicksort(lst, s + 1 ,r)
#첫번째
def partition(lst, l , r):
    p = l
    i = l
    j = r
    while i < j:
        while i < r and lst[i] <= lst[p]:
            i += 1
        while j >l and lst[j] >= lst[p]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[p], lst[j] = lst[j], lst[p]
    return j

#두번째
# def partition(lst,l,r):
#     p = r
#     i = l-1
#     for j in range(l,r):
#         if lst[j]< lst[p]:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#
#     lst[p], lst[i+1] = lst[i+1], lst[p]
#     return i + 1
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(A,0,len(A)-1)
    print(f'#{tc} {A[N//2]}')