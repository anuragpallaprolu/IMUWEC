﻿#!/usr/bin/python
'''
KAFILIMSTER = KALMAN IMPROVED ON STEROIDS
'''

from numpy import *
from pylab import *
from numpy.linalg import inv
import scipy
import numpy as np
import random
from scipy.integrate import quad
from scipy.integrate import simps
#################################
x = np.zeros((2,11))
x_est = np.zeros((2,11))
theta_dot_m = np.zeros((1,11))
data_theta_dot = genfromtxt("gyrox_n.txt")
data_theta = genfromtxt("theta_x_n.txt")
time = data_theta_dot[:,0]
theta_dot_meas = data_theta_dot[:,1]
theta_meas = data_theta[:,1]
dt = 1
dT = np.matrix([[dt],[0]])
F = np.matrix([[1,-dt],[0,1]])
L = random.randrange(1000,2000)
P = np.zeros((2,22))
P[0,0] = L
P[1,1] = L
F_m = np.zeros((22,22))
F_m[0,0] = 1
F_m[0,1] = -dt
F_m[1,1] = 1
P_m = np.zeros((22,22))
Q_m = np.zeros((22,22))
Q_theta = np.zeros((1,11))
Q_theta_dot = np.zeros((1,11))
P_est = np.zeros((22,22))
R = 0.03
H = np.zeros((1,22))
H[0,1] = 1
K = np.zeros((22,1))
z_m = np.zeros((1,11))
H_z = np.zeros((1,2))
H[0,1]=1
x_f = np.zeros((22,11))
x_est_ext = np.zeros((22,11))
#############################
for i in range(0,11):
	x[0,i] = theta_meas[i]
	x[1,i] = theta_dot_meas[i]
	theta_dot_m[0,i] = theta_dot_meas[i]
for i in range(11):
	Q_theta[0,i] = np.var(data_theta[i:,1])
	Q_theta_dot[0,i] = np.var(data_theta_dot[i:,1])


for i in range (0,1):
	for j in range(22):
		P_m[i,j] = P[i,j]

for i in range(0,11):
	Q_m[0,(i)*2] = Q_theta[0,i]
	Q_m[1,(i)*2+1] = Q_theta_dot[0,i]

for i in range(0,11):
	x_est_ext[0,i] = x_est[0,i]	
	x_est_ext[1,i] = x_est[1,i]

###########################
#print dT
#print F
c=0
while(c<11):
	x_est = np.dot(F,x) + np.dot(dT,theta_dot_m)
	#print x_est
	P_est = np.dot(F_m,np.dot(P_m,(F_m.transpose()))) + Q_m*dt
	#print P_est
	S = np.dot(H,np.dot(P_est,(H.transpose()))) + 0.03
	#print S
	K = np.dot(P_est,(H.transpose()))/(S)
	#print K
	z_m = np.dot(H_z,x_est) + np.random.rand(1,11)
	#print z_m
	x_f = x_est_ext + np.dot(K,(np.random.rand(1,11)))
	#print x_f
	P_m = np.dot((np.identity(22) - np.dot(K,H)),P_est)
	print x_f
	#print P_est	
	c=c+1

