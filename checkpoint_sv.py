# For checkpoint

import socket
import time
import json
import picamera
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
matplotlib.use('Agg')

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

def take_camera_pict():
    with picamera.PiCamera() as camera:
        camera.resolution = (256, 192)
        camera.start_preview()
        time.sleep(2)
        timestr = datetime.now().strftime('%Y%m%d%H%M%S')
        image_name = timestr+'.jpg'
        camera.capture(image_name)
        return image_name

def show_pict(file_name):
    img=mpimg.imread(file_name) #image to array
    plt.imshow(img) #array to 2Dfigure
    plt.show()

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

        # take picture by picamera
        image_name = take_camera_pict()

        # show current picture
        # show_pict(image_name)
        
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
