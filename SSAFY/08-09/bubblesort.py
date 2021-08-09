lst= [55, 7, 78, 12, 42]

N = 5
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)