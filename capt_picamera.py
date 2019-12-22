import time
import json
import picamera
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib


def take_camera_pict():
    with picamera.PiCamera() as camera:
        camera.resolution = (512, 384)
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

# take picture by picamera
# print("taking picture")
# image_name = take_camera_pict()