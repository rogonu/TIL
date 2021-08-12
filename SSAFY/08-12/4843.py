import sys
sys.stdin = open('input4843.txt', 'r')

#0 번째는 [0:n-1] 중에 가장 큰 값을 구해서 0번째 데이터와 교환
# 1번째는 [1:n-1]중에 가장 작은 값을 구해서 1번째 데이터와 교환
# 2번째는 [2:n-1] 중에 가장 큰값을 구해서 2번째 데이터와 교환
# i번째는 [i:n-1]중에 i가 짝수이면 가장 큰값 , i가 홀수면 가장 작은 값

# def getmax():

TC = int(input())
for tc in range (1, TC + 1):
    N = int(input())
    Arr = list(map(int, input().split()))
    for i in range(N-1):
        if i % 2 == 0:
            # maxp = getmax(Arr[i:])
            # max_v = Arr[i]
            max_p = i
            for j in range(i, N):
                if Arr[i] < Arr[j]:
                    # max_v = Arr[j]
                    max_p = j
                Arr[max_p], Arr[i] = Arr[i], Arr[max_p]
        else:
            # min_v = Arr[i]
            min_p = i
            for j in range(i, N):
                if Arr[i] > Arr[j]:
                    # min_v = Arr[j]
                    min_p = j
                Arr[min_p], Arr[i] = Arr[i], Arr[min_p]
    for l in range(10):
        print(Arr[l], end = ' ')
    print()
