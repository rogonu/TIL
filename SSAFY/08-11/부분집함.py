짬뽕 = ['오징어', '목이버섯', '면', '청경채']

N = len(짬뽕)
for i in range(1<<4):
    #
    for j in range(N):
        if i & (1<<j) :
            print(짬뽕[j], end=' ')
    print()
