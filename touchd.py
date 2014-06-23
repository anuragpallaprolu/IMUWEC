#Harris Corner Detector
#Using OpenCV and NumPy
#A much more optimized HCD - TOUCHD(TM)
#Tobe On UntouChed Harris Detector
#This is a test TOUCHD run with a large patch and direct optimization procedure
import os
import cv2 as opencv
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
img = cv2.imread("somefile.png")
intensity = np.zeros(512,512)
i,j=0
for i,j in range(1,512):
    intensity[i,j] = img[i,j,0]

#intensity matrix calculated

#Let us take a 30 by 30 patch from the origin

gauss_x = signal.gaussian(30,std=7.5)
gauss_y = signal.gaussian(30,std=7.5)

gauss_2d = np.zeros(30,30)
for i in range(1,30):
    for j in range(1,30):
        gauss_2d[i,j]=gauss_x[i]+gauss_y[j]

#we need to write a minimizing routine

def E(u,v):
    global gauss_2d, intensity
    for i,j in range(1,30):
        p_sum[i,j] = gauss_2d[i,j]*((intensity[i+u,j+v] - intensity[u,v])^2)
        t_sum = t_sum + p_sum[i,j]
    return t_sum

print E(1,2)
