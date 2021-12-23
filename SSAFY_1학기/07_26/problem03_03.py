import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_number_case(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    number = list(map(str,range(10)))          # number는 0부터 9까지의 수를 문자열로 변형시켜 list로 만듬
    password = []                              # password 의 빈 리스트를 만들어 data['password'] 의 값을 따로따로 리스트에 저장 이따 저장된 값은 전부 문자열
    for i in data['password']:
        password.append(i)
    value = []                       
    for j in password:            # password 에 저장된 값들이 각각 number 안에 있는지 확인하고
        if j in number:           # number 안에 있다면 True 값을 value 에 넣는다.
            value.append(True)
    if True in value:             # data['password'] 값에 숫자가 있었다면 True 값이 value 안에 있을것이므로 True 반환
        return True               # data['password'] 값에 숫자가 없었다면 True 값이 value 안에 없을것이므로 False 반환
    else:
        return False
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = open('problem03_data.json', encoding='UTF8')
    user_data = json.load(user_data)
    print(check_password_number_case(user_data))
    # True