lst = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * 5
N = len(lst)
TEMP = [0] * N

for k in lst:
    cnt[k] += 1
for i in range((len(cnt))-1):
    cnt[i+1] = cnt[i] + cnt[i+1]
for j in range(N-1, -1, -1):
    # p1 = lst[j]
    # p2 = cnt[p1]
    # TEMP[p2] = p1
    # cnt[p1] -= 1
    cnt[lst[j]] -= 1
    TEMP[cnt[lst[j]]] = lst[j]

print(TEMP)