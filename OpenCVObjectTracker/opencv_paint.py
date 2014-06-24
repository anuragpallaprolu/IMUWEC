import cv2 as opencv
import numpy as np

#Paint program for future PyOS
#The draw circle function based on a function callback
#a callback is a function in a function
def draw_circle(event,x,y,flag,param):
    if event == opencv.EVENT_LBUTTONDBLCLK:
            opencv.circle(img, (x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3), np.uint8)
opencv.namedWindow('base')
opencv.setMouseCallback('base', draw_circle);

while(True):
    opencv.imshow('base',img)
    if opencv.waitKey(20) == 27:
        break

opencv.destroyAllWindows()
