﻿#!/usr/bin/python
from numpy import *
from pylab import *
import scipy
from scipy.integrate import quad
from scipy.integrate import simps

data = genfromtxt('gyrox_n.txt')
time   = data[:,0]  # Python indices are (row,col) as in linalg
gyrox = data[:,1]  # Creates arrays for first two column
i = 1;
for i in range(1,6):
	for x in xrange(0,i):
			data = genfromtxt('gyrox_n.txt')
			time = data[i:,0]
			gyrox = data[i:,1]
			print scipy.integrate.simps(gyrox,time)
			i = i + 1
plot(time,gyrox)
grid(True)
# Save the figure in a separate file
savefig('read_and_plot_data.png')

# Draw the plot to the screen
show()

print scipy.integrate.simps(gyrox,time)
