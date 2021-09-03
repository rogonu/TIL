import requests
import random
from django.shortcuts import render
# Create your views here.

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    response = requests.get(url)
    lotto = response.json()
    winno = []
    for i in range(1, 7):
        winno.append(lotto[f'drwtNo{i}'])
    bonusn = lotto['bnusNo']
    result = {'1등': 0, '2등': 0,'3등': 0,'4등': 0,'5등': 0}
    for i in range(1000):
        cnt = 0
        bon = 0
        my_numbers = random.sample(range(1,46), 6)
        for j in range(len(my_numbers)):
            if my_numbers[j] in winno:
                cnt +=1
            if my_numbers[j] == bonusn:
                bon +=1
        if cnt == 6:
            result['1등'] += 1
        elif cnt == 5:
            if bonusn == 1:
                result['2등'] += 1
            else:
                result['3등'] += 1
        elif cnt == 4:
            result['4등'] += 1
        elif cnt ==3 :
            result['5등'] += 1
    context ={
        'lotto' : lotto,
        'winno' : winno,
        'bonusn' : bonusn,
        'result' : result
    }
    return render(request, 'pages/lotto.html', context)