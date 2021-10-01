TC = int(input())
for tc in range(1, TC + 1):
    num, change = input().split()
    num = list(map(int, num))

    for i in range(int(change)):
        if num[i] < max(num):
            temp = num[i]
            max_pos = num.index((max(num)))
            num[i]= num[max_pos]
            num[max_pos] = temp
    print(num)
