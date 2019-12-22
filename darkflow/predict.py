from darkflow.net.build import TFNet
import cv2
import numpy as np

options = {"model": "cfg/yolov2-tiny-voc.cfg", "load": "bin/yolov2-tiny-voc.weights", "threshold": 0.1}

tfnet = TFNet(options)

class_names = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
              'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
                            'dog', 'horse', 'motorbike', 'person', 'pottedplant',
                                          'sheep', 'sofa', 'train', 'tvmonitor']

imgcv = cv2.imread("./sample_dog.jpg")
result = tfnet.return_predict(imgcv)
print(result)
