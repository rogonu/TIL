import sys
sys.stdin = open('input210813.txt', 'r')

num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
TC = int(input())
for tc in range(1, TC+1):
    a, b = input().split()
    nums_len = int(b)
    nums = list(input().split())

    result = [[] for _ in range(len(num_str))]
    for num in nums:
        for i in range(len(num_str)):
            if num == num_str[i]:
                result[i].append(num)
    print(f'#{tc}')
    for j in range(len(num_str)):
        print(' '.join(result[j]))

