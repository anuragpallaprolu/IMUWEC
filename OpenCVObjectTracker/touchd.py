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
import matplotlib as ml
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


img = opencv.imread("frame31.png")
opencv.imshow('image',img)
opencv.waitKey(0)
opencv.destroyAllWindows()
intensity = np.zeros((50,50))
i=0
j=0
for i in range(1,50):
    for j in range(1,50):
        intensity[i,j] = img[i,j,0]

#intensity matrix calculated

#Let us take a 30 by 30 patch from the origin

gauss_x = signal.gaussian(30,std=7.5)
gauss_y = signal.gaussian(30,std=7.5)

gauss_2d = np.zeros((30,30))
for i in range(1,30):
    for j in range(1,30):
        gauss_2d[i,j]=gauss_x[i]+gauss_y[j]


unit_2d = np.zeros((640,480))
for i in range(1,640):
    for j in range(1,480):
        if i > 30 or j > 30:
            unit_2d[i,j]=0
        else:
            unit_2d[i,j]=1
    
    
#we need to write a minimizing routine
p_sum = np.zeros((30,30))

def t_sum(u,v):
    return 0

def E(u,v):
   global gauss_2d, intensity
   t_sum_new = t_sum(5,3)
   for i in range(1,30):
        for j in range(1,30):
            p_sum[i,j] = gauss_2d[i,j]*((intensity[i+u,j+v] - intensity[i,j])**2)
            #print p_sum[i,j]
            t_sum_new = t_sum_new + p_sum[i,j]
    
   return t_sum_new

print "Sample E Values"
for i in range(1,5):
    for j in range(1,5):
        print E(i,j)

print "End E Values"

E_matrix = np.zeros((30,30))
for i in range(1,15):
    for j in range(1,15):
        E_matrix[i,j] = E(i,j)
        
fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(E_matrix)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
#Why write one when you can basinhop!
#x0 = np.matrix('2 5')
#x1 = np.matrix('3 4')
#E_op_result = optimize.basinhopping(E,x0,x1)
#print E_op_result.x
#print E_op_result.success
#print E_op_result.status
