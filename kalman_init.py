#!/usr/bin/python
'''

'''
from numpy import *
from pylab import *
import scipy
import statistics
from scipy.integrate import quad
from scipy.integrate import simps

data_theta_dot = genfromtxt("gyrox_n.txt")
data_theta = genfromtxt("theta_x_n.txt")
time = data_theta_dot[:,0]
theta_dot = data_theta_dot[:,1]
theta = data_theta[:,1]
bias[0] = 0.52
dt = 1
theta_est[i] = theta[i] + dt*(bias[i])
P_00[i] = P_00[i]+dt*(dt*P_11[i-1]-P_01[i-1]-P_10[i-1] + var_theta)
P_01[i] -= dt*P_11[i-1]
P_10[i] -= dt*P_11[i-1]
P_11[i] += var_bias*dt
y[i] = theta_est[i] - theta[i]
S[i] = P_00[i] + 0.03
K_0[i] = P_00[i]/S[i]
K_1[i] = P_10[i]/S[i]
theta_est[i] = theta_est[i-1]+K_0[i]*y[i]
bias[i]= bias[i-1] + K_1[i]*y[i]

