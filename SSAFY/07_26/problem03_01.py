import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_password_verified(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if data['password'] == data ['password_confirm']:    # data['password']값과 data['password_confirm'] 값이 같으면 True 아니면 False 를 작성했음.
        return True
    else:
        return False

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = open('problem03_data.json', encoding='UTF8')
    user_data = json.load(user_data)
    print(is_password_verified(user_data))
    # True
    