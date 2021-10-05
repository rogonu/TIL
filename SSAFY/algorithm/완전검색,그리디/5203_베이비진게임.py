TC = int(input())
for tc in range(1, TC + 1):
    nums = list(map(int, input().split()))
    player_1 = []
    player_2 = []

    res = -1
    cnt = 0

    while res == -1 and len(player_1) < 6:
        score_1 = 0
        score_2 = 0
        player_1.append(nums[2 * cnt])
        player_2.append(nums[2 * cnt + 1])
        player_1.sort()
        player_2.sort()
        for i in range(len(player_1)):
            if player_1[i] + 1 in player_1 and player_1[i] + 2 in player_1:
                score_1 += 1
            if player_1.count(player_1[i]) >= 3:
                score_1 += 1
        for j in range(len(player_2)):
            if player_2[j] + 1 in player_2 and player_2[j] + 2 in player_2:
                score_2 += 1
            if player_2.count(player_2[j]) >= 3:
                score_2 += 1
        cnt += 1
        if score_1 > score_2:
            res = 1

        elif score_2 > score_1:
            res = 2

        elif score_1 != 0 and score_1 == score_2:
            res = 0

    if res == -1:
        res = 0
    print(f'#{tc} {res}')
