import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over(movie):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if movie['user_rating'] >= 8:              # moive['user_rating']의 값이 평점이므로 평점이 8이상이면 True 아니면 False 인 함수를 만든다.
        return True
    else:
        return False
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # True