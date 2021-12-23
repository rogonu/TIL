def mergesort(lst):
    global cnt
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    left = mergesort(lst[0:m])
    right = mergesort((lst[m:]))
    if left[-1] < right[-1]:
        cnt += 1
    res = merge(left, right)
    return res

def merge(left, right):
    l = r = 0
    res =[]
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    mergesort(A)
    print(f'#{tc} {A[N//2]} {cnt}')