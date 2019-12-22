import socket
import json
import webbrowser

# read config file
f = open("config_cli.json", "r")
config = f.read()
config = json.loads(config) # json to dict
config_str = json.dumps(config)

M_SIZE = 1024

# Serverのアドレスを用意。Serverのアドレスは確認しておく必要がある。
# serv_address = ('127.0.0.1', 8890)
address = config["sv_ip"]
port = config["sv_port"]
# serv_address = ('192.168.11.5', 8890)
serv_address = (address, port)

# ①ソケットを作成する
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        # ②messageを送信する
        # print('Input any messages, Type [end] to exit')
        print(f'sending message to {address}, {port}')
        # message = input()
        message = config_str
        if message != 'end':
            # send_len = sock.sendto(message.encode('utf-8'), serv_address)
            send_len = sock.sendto(message.encode('utf-8'), serv_address)
            # ※sendtoメソッドはkeyword arguments(address=serv_addressのような形式)を受け付けないので注意

            # ③Serverからのmessageを受付開始
            print('Waiting response from Server')
            rx_meesage, addr = sock.recvfrom(M_SIZE)
            print(f"[Server]: {rx_meesage.decode(encoding='utf-8')}")

            # TODO: Webにアクセス
            dict_meesage = json.loads(rx_meesage)
            url = dict_meesage["url"][:-1] + "?cp-id=" + dict_meesage["cp-id"]
            webbrowser.open(url)

            break

        else:
            print('closing socket')
            sock.close()
            print('done')
            break

    except KeyboardInterrupt:
        print('closing socket')
        sock.close()
        print('done')
        break
