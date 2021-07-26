import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def history(movie):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if '과거' in movie['overview']:                # 과거라는 글자가 줄거리 안에 있으면 True 아니면 False 이므로 if 문을 이용하여 '과거'라는 문자열이
        return True                                # movie['overview']안에 있으면 True 아니면 False 라는 함수를 작성했음
    else:
        return False

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # False