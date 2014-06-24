#Harris Corner Detector
#Using OpenCV and NumPy
#A much more optimized HCD - TOUCHD(TM)
#Tobe On UntouChed Harris Detector
#This is a test TOUCHD run with a large patch and direct optimization procedure
import os
import cv2 as opencv
import numpy as np
from scipy import optimize
from scipy import signal
from scipy.fftpack import fft, fftshift
img = opencv.imread("drawing.png")
#opencv.imshow('image',img)
intensity = np.zeros((512,512))
i=0
j=0
for i in range(1,512):
    for j in range(1,512):
        intensity[i,j] = img[i,j,0]

#intensity matrix calculated

#Let us take a 30 by 30 patch from the origin

gauss_x = signal.gaussian(30,std=7.5)
gauss_y = signal.gaussian(30,std=7.5)

gauss_2d = np.zeros((30,30))
for i in range(1,30):
    for j in range(1,30):
        gauss_2d[i,j]=gauss_x[i]+gauss_y[j]


unit_2d = np.zeros((512,512))
for i in range(1,512):
    for j in range(1,512):
        if i > 30 or j > 30:
            unit_2d[i,j]=0
        else:
            unit_2d[i,j]=1
    
    
#we need to write a minimizing routine
p_sum = np.zeros((30,30))

#def t_sum(u,v):
#    return 0

#def E(u,v):
#    global gauss_2d, intensity
#t_sum_new = t_sum(5,3)
for i in range(1,30):
    for j in range(1,30):
        p_sum[i,j] = unit_2d[i,j]*((intensity[i+5,j+3] - intensity[5,3])**2)
        print p_sum[i,j]
       # t_sum_new = t_sum_new + p_sum[i,j]
    
#    return t_sum_new

#print E(1,1)
#Why write one when you can basinhop!
#x0 = np.matrix('2 5')
#x1 = np.matrix('3 4')
#E_op_result = optimize.basinhopping(E,x0,x1)
#print E_op_result.x
#print E_op_result.success
#print E_op_result.status
