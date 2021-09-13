import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU03_NOHGEONWOO'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send(('%d/%d' % (CODE_REQUEST, CODE_REQUEST)).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = float(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %f, %f' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 gameData에 들어갑니다.
    #   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) gameData.balls[0][0]: 흰 공의 X좌표
    #         gameData.balls[0][1]: 흰 공의 Y좌표
    #         gameData.balls[1][0]: 1번 공의 X좌표
    #         gameData.balls[4][0]: 4번 공의 X좌표
    #         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.
    # if gameData.order == 1:
    res = 1000

    firstPlayer = [1, 3]
    secondPlayer = [2, 4]

    player = firstPlayer if gameData.order == 1 else secondPlayer

    if gameData.balls[player[0]][0] > 0:
        for j in range(6):
            rkfh = HOLES[j][0] - gameData.balls[player[0]][0]
            tpfh = HOLES[j][1] - gameData.balls[player[0]][1]
            dist = math.sqrt(rkfh ** 2 + tpfh ** 2)
            if dist < res:
                res = dist
                hole_number = j
                ball_number = player[0]
    elif gameData.balls[player[1]][0] > 0:
        for j in range(6):
            rkfh = HOLES[j][0] - gameData.balls[player[1]][0]
            tpfh = HOLES[j][1] - gameData.balls[player[1]][1]
            dist = math.sqrt(rkfh ** 2 + tpfh ** 2)
            if dist < res:
                res = dist
                hole_number = j
                ball_number = player[1]
    else:
        for j in range(6):
            rkfh = HOLES[j][0] - gameData.balls[5][0]
            tpfh = HOLES[j][1] - gameData.balls[5][1]
            dist = math.sqrt(rkfh ** 2 + tpfh ** 2)
            if dist < res:
                res = dist
                hole_number = j
                ball_number = 5
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수

    # 각도 구하기 위한 new target 설정
    targetBall_x = gameData.balls[ball_number][0]
    targetBall_y = gameData.balls[ball_number][1]
    rkfh = abs(HOLES[hole_number][0] - targetBall_x)
    tpfh = abs(HOLES[hole_number][1] - targetBall_y)
    l = math.sqrt(rkfh ** 2 + tpfh ** 2)

    ext_x = abs((l + 5.73) * rkfh) / l - rkfh
    ext_y = abs((l + 5.73) * tpfh) / l - tpfh
    if HOLES[hole_number][0] < targetBall_x:
        new_target_x = targetBall_x + ext_x
    elif HOLES[hole_number][0] == targetBall_x:
        new_target_x = targetBall_x
    else:
        new_target_x = targetBall_x - ext_x
    if HOLES[hole_number][1] < targetBall_y:
        new_target_y = targetBall_y + ext_y
    elif HOLES[hole_number][1] == targetBall_y:
        new_target_y = targetBall_y
    else:
        new_target_y = targetBall_y - ext_y

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(new_target_x - whiteBall_x)
    height = abs(new_target_y - whiteBall_y)

    # def hall_choice(bn):
    #     res = 1000
    #     for i in range(6):
    #         rkfh = HOLES[i][0] - gameData.balls[bn][0]
    #         tpfh = HOLES[i][1] - gameData.balls[bn][1]
    #         dist = math.sqrt(rkfh ** 2 + tpfh ** 2)
    #         if dist < res:
    #             res = dist
    #             hole_number = i
    #     return hole_number
    def get_degree():
        x = new_target_x - whiteBall_x
        y = new_target_y - whiteBall_y
        radian = math.atan2(x, y)
        angle = (360 + math.degrees(radian)) % 360
        return angle

    angle = get_degree()
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width ** 2 + height ** 2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = 10 if distance * 0.8 < 10 else distance * 0.8

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()
