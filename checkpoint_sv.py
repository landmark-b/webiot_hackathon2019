# For checkpoint

import socket
import time
import json

M_SIZE = 1024

# 
# host = '127.0.0.1'
host = '192.168.11.5'
port = 8890

locaddr = (host, port)

# read config file
f = open("config.json", "r")
config = f.read()
config = json.loads(config)
config_str = json.dumps(config)

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
print('create socket')

sock.bind(locaddr)

while True:
    try :
        print('Waiting message')
        message, cli_addr = sock.recvfrom(M_SIZE)
        message = message.decode(encoding='utf-8')
        print('Received message is [{}]'.format(message))

        time.sleep(1)

        print('Send response to Client')

        # sock.sendto('Success to receive message'.encode(encoding='utf-8'), cli_addr) 
        sock.sendto(config_str.encode(encoding='utf-8'), cli_addr)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
